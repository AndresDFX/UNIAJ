# -*- coding: utf-8 -*-
"""Exporta los archivos nativos de Google del workspace a su equivalente Microsoft.

Por que existe
--------------
Buena parte del material de Programacion II y Seminario de Sistemas todavia vive
como documento nativo de Google (.gdoc / .gslides). En disco esos archivos NO son
documentos: son punteros que el sistema de archivos ni siquiera puede leer
("Invalid request code"), asi que no se pueden versionar, ni abrir sin internet,
ni procesar con python-docx/python-pptx.

Este script los baja convertidos a .docx / .pptx / .xlsx AL LADO del puntero,
sin borrar nada: el original de Google sigue existiendo en Drive.

    .gdoc    -> .docx
    .gslides -> .pptx
    .gsheet  -> .xlsx

Como identifica cada archivo
----------------------------
El ID de Drive se saca de la base de metadatos local de Google Drive for Desktop
(`metadata_sqlite_db`), cruzando el nombre exacto del archivo + su tipo MIME.
No hace falta pedirle nada a Drive para eso.

Autenticacion — dos modos
-------------------------
**Modo gcloud (recomendado, es el que funciona).** Google BLOQUEA el uso de sus
propios client_id del SDK desde una app de terceros: el navegador muestra
"aplicacion bloqueada". La salida es dejar que autentique el propio gcloud, que
si es una app verificada de Google:

    gcloud config configurations create drive-export --no-activate
    gcloud --configuration=drive-export auth login --enable-gdrive-access
    python config/slides/exportar_google_a_office.py --gcloud

Se usa una CONFIGURACION APARTE a proposito: asi la cuenta activa por defecto
(la cuenta de servicio corporativa) queda intacta. El token dura ~1 h; si expira
a mitad, se vuelve a correr el script y continua donde quedo.

**Modo OAuth propio.** Solo sirve con un client_id creado por el usuario en su
propio proyecto de Google Cloud (APIs y servicios > Credenciales > ID de cliente
de OAuth > App de escritorio) exportado en DRIVE_CLIENT_ID / DRIVE_CLIENT_SECRET.
El token queda en `config/slides/.drive_token.json` (ignorado por git).

En ambos casos el scope es de SOLO LECTURA. NO se usa la cuenta de servicio
corporativa: no tiene acceso a este Drive personal y no corresponde usarla.

Uso
---
    python config/slides/exportar_google_a_office.py --gcloud    # token de gcloud
    python config/slides/exportar_google_a_office.py --dry-run   # solo lista
    python config/slides/exportar_google_a_office.py --force     # re-exporta todo
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
import sqlite3
import sys
import time
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SLIDES = Path(__file__).resolve().parent
TOKEN_PATH = SLIDES / ".drive_token.json"

SCOPES = ["https://www.googleapis.com/auth/drive.readonly"]

GCLOUD_CONFIG = "drive-export"  # configuracion aislada: no toca la cuenta activa por defecto

EXPORT = {
    ".gdoc": ("application/vnd.google-apps.document",
              "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
              ".docx"),
    ".gslides": ("application/vnd.google-apps.presentation",
                 "application/vnd.openxmlformats-officedocument.presentationml.presentation",
                 ".pptx"),
    ".gsheet": ("application/vnd.google-apps.spreadsheet",
                "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                ".xlsx"),
}


def _norm(s: str) -> str:
    """Drive y NTFS normalizan Unicode distinto (NFC vs NFD): sin esto, todo
    nombre con tilde falla el match."""
    return unicodedata.normalize("NFC", (s or "").strip()).lower()


def _drivefs_db() -> Path | None:
    base = Path(os.environ.get("LOCALAPPDATA", "")) / "Google" / "DriveFS"
    if not base.is_dir():
        return None
    for d in base.iterdir():
        if d.is_dir() and d.name.isdigit() and (d / "metadata_sqlite_db").exists():
            return d / "metadata_sqlite_db"
    return None


def mapear_ids(tmp_dir: Path) -> tuple[list[dict], list[dict]]:
    """Devuelve (mapeados, ambiguos) cruzando disco <-> metadatos de Drive."""
    src = _drivefs_db()
    if not src:
        sys.exit("No se encontro la base de metadatos de Google Drive for Desktop.")
    tmp_dir.mkdir(parents=True, exist_ok=True)
    dst = tmp_dir / "meta_copy.db"
    for ext in ("", "-wal", "-shm"):
        if (p := Path(str(src) + ext)).exists():
            try:
                shutil.copy2(p, str(dst) + ext)
            except OSError:
                pass

    con = sqlite3.connect(dst)
    cur = con.cursor()
    cur.execute("SELECT id, local_title, mime_type, trashed FROM items "
                "WHERE mime_type LIKE 'application/vnd.google-apps.%'")
    idx: dict[tuple[str, str], list[str]] = {}
    for _id, title, mime, trashed in cur.fetchall():
        if not trashed:
            idx.setdefault((_norm(title), mime), []).append(_id)
    con.close()

    punteros = [p for p in ROOT.rglob("*")
                if p.suffix.lower() in EXPORT and ".git" not in p.parts]
    mapeados, ambiguos = [], []
    for p in punteros:
        g_mime, off_mime, off_ext = EXPORT[p.suffix.lower()]
        cands = idx.get((_norm(p.name), g_mime), [])
        destino = p.with_suffix(off_ext)
        reg = {"path": str(p), "destino": str(destino),
               "mime_export": off_mime, "ids": cands}
        if len(cands) == 1:
            reg["id"] = cands[0]
            mapeados.append(reg)
        elif cands:
            ambiguos.append(reg)
    return mapeados, ambiguos


def _token_de_gcloud() -> str:
    """Access token de la configuracion aislada de gcloud (no la corporativa)."""
    import subprocess

    # En Windows gcloud es gcloud.cmd: subprocess sin shell NO aplica PATHEXT,
    # asi que hay que resolver la ruta real con which().
    exe = shutil.which("gcloud") or shutil.which("gcloud.cmd")
    if not exe:
        sys.exit("No se encontro 'gcloud' en el PATH.")
    cmd = [exe, f"--configuration={GCLOUD_CONFIG}", "auth", "print-access-token"]
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
    except OSError as e:
        sys.exit(f"No se pudo ejecutar gcloud: {e}")
    tok = (r.stdout or "").strip()
    if r.returncode != 0 or not tok:
        sys.exit(
            "No hay sesion de Drive en gcloud. Corre primero:\n\n"
            f"  gcloud config configurations create {GCLOUD_CONFIG} --no-activate\n"
            f"  gcloud --configuration={GCLOUD_CONFIG} auth login --enable-gdrive-access\n\n"
            f"Detalle: {(r.stderr or '').strip()[:300]}"
        )
    _verificar_token(tok)
    return tok


def _verificar_token(tok: str) -> None:
    """Salvaguarda: en una VM de GCE, gcloud devuelve el token de la CUENTA DE
    SERVICIO del metadata server aunque se pida otra configuracion. Ese token es
    corporativo, no tiene scope de Drive y no debe usarse contra un Drive
    personal. Se verifica identidad y scope ANTES de tocar ningun archivo."""
    import urllib.request

    try:
        with urllib.request.urlopen(
            "https://www.googleapis.com/oauth2/v3/tokeninfo?access_token=" + tok, timeout=30
        ) as resp:
            info = json.loads(resp.read().decode("utf-8"))
    except Exception as e:
        sys.exit(f"No se pudo verificar el token ({e}). Se aborta por seguridad.")

    email = info.get("email", "")
    scopes = info.get("scope", "")
    if "drive" not in scopes:
        sys.exit(
            "El token de gcloud NO tiene permiso de Drive.\n"
            f"  identidad: {email or '(cuenta de servicio / metadata de GCE)'}\n"
            f"  scopes   : {scopes[:120]}\n\n"
            "Esto pasa porque en esta VM gcloud devuelve la credencial corporativa\n"
            "del metadata server. Autentica TU cuenta con acceso a Drive:\n\n"
            f"  gcloud --configuration={GCLOUD_CONFIG} auth login --enable-gdrive-access\n"
        )
    if email.endswith(".gserviceaccount.com"):
        sys.exit(
            f"El token pertenece a una CUENTA DE SERVICIO ({email}).\n"
            "No se usara una identidad corporativa para leer un Drive personal.\n"
            f"Autentica tu cuenta: gcloud --configuration={GCLOUD_CONFIG} auth login --enable-gdrive-access"
        )
    print(f">> Exportando como: {email}\n")


def get_service(usar_gcloud: bool):
    from google.oauth2.credentials import Credentials
    from googleapiclient.discovery import build

    if usar_gcloud:
        creds = Credentials(token=_token_de_gcloud())
        return build("drive", "v3", credentials=creds, cache_discovery=False)

    from google.auth.transport.requests import Request
    from google_auth_oauthlib.flow import InstalledAppFlow

    cid = os.environ.get("DRIVE_CLIENT_ID")
    csec = os.environ.get("DRIVE_CLIENT_SECRET")
    creds = None
    if TOKEN_PATH.exists():
        try:
            creds = Credentials.from_authorized_user_file(str(TOKEN_PATH), SCOPES)
        except Exception:
            creds = None
    if creds and creds.expired and creds.refresh_token:
        try:
            creds.refresh(Request())
        except Exception:
            creds = None
    if not creds or not creds.valid:
        if not (cid and csec):
            sys.exit(
                "Sin credenciales OAuth propias.\n\n"
                "Google bloquea sus client_id del SDK usados desde otra app\n"
                "(pantalla 'aplicacion bloqueada'). Usa el modo gcloud:\n\n"
                f"  gcloud config configurations create {GCLOUD_CONFIG} --no-activate\n"
                f"  gcloud --configuration={GCLOUD_CONFIG} auth login --enable-gdrive-access\n"
                "  python config/slides/exportar_google_a_office.py --gcloud\n\n"
                "O define DRIVE_CLIENT_ID / DRIVE_CLIENT_SECRET de un cliente de\n"
                "escritorio creado en tu propio proyecto de Google Cloud."
            )
        cfg = {"installed": {
            "client_id": cid, "client_secret": csec,
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "redirect_uris": ["http://localhost"]}}
        flow = InstalledAppFlow.from_client_config(cfg, SCOPES)
        creds = flow.run_local_server(port=0)
        TOKEN_PATH.write_text(creds.to_json(), encoding="utf-8")
        print(f">> Token guardado en {TOKEN_PATH.name} (reutilizable).\n")
    return build("drive", "v3", credentials=creds, cache_discovery=False)


def exportar(svc, file_id: str, mime: str, destino: Path) -> int:
    """Descarga el archivo convertido. Devuelve bytes escritos."""
    from googleapiclient.http import MediaIoBaseDownload
    import io

    req = svc.files().export_media(fileId=file_id, mimeType=mime)
    buf = io.BytesIO()
    dl = MediaIoBaseDownload(buf, req, chunksize=5 * 1024 * 1024)
    done = False
    while not done:
        _status, done = dl.next_chunk()
    data = buf.getvalue()
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_bytes(data)
    return len(data)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true", help="solo listar, no descargar")
    ap.add_argument("--force", action="store_true", help="re-exportar aunque ya exista")
    ap.add_argument("--gcloud", action="store_true",
                    help="usar el access token de la configuracion gcloud aislada (recomendado)")
    args = ap.parse_args()

    tmp = SLIDES / "_tmp_drivemeta"
    mapeados, ambiguos = mapear_ids(tmp)
    print(f"Punteros de Google encontrados: {len(mapeados) + len(ambiguos)}")
    print(f"  con ID unico : {len(mapeados)}")
    print(f"  ambiguos     : {len(ambiguos)} (mismo nombre en varias carpetas)")

    pend = [m for m in mapeados if args.force or not Path(m["destino"]).exists()]
    print(f"  por exportar : {len(pend)}\n")

    if args.dry_run:
        for m in pend[:20]:
            print("  ->", Path(m["destino"]).relative_to(ROOT))
        if len(pend) > 20:
            print(f"  ... y {len(pend) - 20} mas")
        return

    if not pend:
        print("Nada que exportar.")
        return

    svc = get_service(args.gcloud)
    ok = fail = 0
    fallidos = []
    for i, m in enumerate(pend, 1):
        destino = Path(m["destino"])
        rel = destino.relative_to(ROOT)
        for intento in (1, 2, 3):
            try:
                n = exportar(svc, m["id"], m["mime_export"], destino)
                print(f"[{i}/{len(pend)}] OK  {n/1024:7.0f} KB  {rel}")
                ok += 1
                break
            except Exception as e:
                if intento == 3:
                    print(f"[{i}/{len(pend)}] FALLA  {rel}\n        {type(e).__name__}: {str(e)[:120]}")
                    fallidos.append({"archivo": str(rel), "error": str(e)[:200]})
                    fail += 1
                else:
                    time.sleep(2 * intento)  # backoff ante 429/5xx

    print(f"\nExportados: {ok}   Fallidos: {fail}")
    if ambiguos:
        print(f"\nSin exportar por nombre ambiguo ({len(ambiguos)}) — revisar a mano:")
        for a in ambiguos:
            print("  ", Path(a['path']).relative_to(ROOT), f"({len(a['ids'])} candidatos)")
    if fallidos:
        (SLIDES / "_export_fallidos.json").write_text(
            json.dumps(fallidos, indent=1, ensure_ascii=False), encoding="utf-8")


if __name__ == "__main__":
    main()
