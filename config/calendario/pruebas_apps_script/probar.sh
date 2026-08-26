#!/usr/bin/env bash
# Ejecuta las pruebas de los Apps Script generados. Necesita node y los .gs ya generados
# (python config/calendario/generar_apps_script_encuentros.py).
set -u
cd "$(dirname "$0")"
RAIZ="$(cd ../../.. && pwd)"
PERIODO="${1:-2026-2}"
malo=0

CONS="$RAIZ/_privado/$PERIODO/CrearEncuentros - TODO EL SEMESTRE $PERIODO.gs"
if [ -f "$CONS" ]; then
  node probar.js "$CONS" || malo=1
else
  echo "no encuentro el consolidado: $CONS"; malo=1
fi

for gs in "$RAIZ"/*/"Plan curso/$PERIODO/_privado/CrearEncuentros - "*.gs; do
  [ -f "$gs" ] || continue
  node probar_curso.js "$gs" || malo=1
done

echo
[ $malo -eq 0 ] && echo "TODO OK" || echo "HUBO FALLOS"
exit $malo
