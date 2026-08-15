# Lab Floci — script estudiante (MVP · borrador)

Curso: **Arquitectura de Sistemas Computacionales** · PI **CloudLite** · 2026-2  
Plan de viabilidad: `../PLAN_VIABILIDAD_FLOCI_2026-2.md`

## Objetivo
En **1 comando** levantar un emulador cloud local (**sin cuenta, sin tarjeta**) y dejar listo un smoke test de object storage.

## Prerrequisitos
- Docker Desktop / Engine **en ejecución**, **o**
- Sesión en [LabEx Docker Playground](https://labex.io) / Killercoda (camino solo navegador).

## Uso rápido (Windows)
```powershell
cd "...\Plan curso\2026-2\scripts"
.\lab-floci.ps1 -Cloud aws
```

Otras nubes:
```powershell
.\lab-floci.ps1 -Cloud az
.\lab-floci.ps1 -Cloud gcp
.\lab-floci.ps1 -Cloud oci
```

Detener:
```powershell
.\lab-floci.ps1 -Cloud aws -Stop
```

## Uso rápido (Linux / macOS / Git Bash)
```bash
chmod +x lab-floci.sh
./lab-floci.sh aws
./lab-floci.sh az
./lab-floci.sh gcp
./lab-floci.sh oci
./lab-floci.sh aws --stop
```

## Camino B — LabEx Docker Playground (sin instalar en el PC)
```bash
docker run --rm -d --name uniajc-floci -p 4566:4566 \
  -v /var/run/docker.sock:/var/run/docker.sock \
  floci/floci:latest

curl -s http://localhost:4566/_floci/health || curl -s http://localhost:4566/_localstack/health
```

Luego (si hay AWS CLI en el lab):
```bash
export AWS_ENDPOINT_URL=http://localhost:4566
export AWS_ACCESS_KEY_ID=test AWS_SECRET_ACCESS_KEY=test AWS_DEFAULT_REGION=us-east-1
aws s3 mb s3://cloudlite-lab
echo "hola CloudLite" > hola.txt
aws s3 cp hola.txt s3://cloudlite-lab/
aws s3 ls s3://cloudlite-lab/
```

## Qué hace el script
1. Comprueba `docker info`.
2. `docker pull` de la imagen de la nube elegida.
3. Arranca el contenedor `uniajc-floci-<cloud>` con el puerto correcto.
4. Espera health / imprime variables de entorno.
5. Intenta smoke test (bucket + objeto) si encuentra la CLI correspondiente.

## Fuentes oficiales
- https://floci.io/
- https://github.com/floci-io/floci
- https://github.com/floci-io/floci-az
- https://github.com/floci-io/floci-gcp
- https://github.com/floci-io/floci-oci

## Nota docente
Borrador de piloto. No es requisito del curso hasta aprobación. Preferir tag fijo de imagen tras la prueba en aula.
