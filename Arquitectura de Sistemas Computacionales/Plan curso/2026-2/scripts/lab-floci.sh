#!/usr/bin/env bash
# MVP UNIAJC — arranca Floci (emulador cloud local) para el lab CloudLite.
# Uso: ./lab-floci.sh [aws|az|gcp|oci] [--stop]
set -euo pipefail

CLOUD="${1:-aws}"
STOP=0
if [[ "${2:-}" == "--stop" ]] || [[ "${1:-}" == "--stop" ]]; then
  STOP=1
  [[ "${1:-}" == "--stop" ]] && CLOUD="aws"
fi

case "$CLOUD" in
  aws) IMAGE="floci/floci:latest";     PORT=4566; NAME="uniajc-floci-aws"; SOCK=1 ;;
  az)  IMAGE="floci/floci-az:latest";  PORT=4577; NAME="uniajc-floci-az";  SOCK=0 ;;
  gcp) IMAGE="floci/floci-gcp:latest"; PORT=4588; NAME="uniajc-floci-gcp"; SOCK=0 ;;
  oci) IMAGE="floci/floci-oci:latest"; PORT=4599; NAME="uniajc-floci-oci"; SOCK=1 ;;
  *)
    echo "Uso: $0 [aws|az|gcp|oci] [--stop]"
    exit 1
    ;;
esac

echo ""
echo "UNIAJC · CloudLite · Lab Floci ($CLOUD)"
echo "Emulador local · MIT · sin cuenta · sin tarjeta"
echo ""

if ! docker info >/dev/null 2>&1; then
  echo "ERROR: Docker no responde."
  echo "Opciones:"
  echo "  1) Inicia Docker y reintenta."
  echo "  2) Camino navegador: LabEx Docker Playground / Killercoda (ver README.md)."
  exit 1
fi

if [[ "$STOP" -eq 1 ]]; then
  echo "Deteniendo $NAME..."
  docker rm -f "$NAME" >/dev/null 2>&1 || true
  echo "Listo."
  exit 0
fi

docker rm -f "$NAME" >/dev/null 2>&1 || true

echo "1/3 Pull $IMAGE ..."
docker pull "$IMAGE"

echo "2/3 Arrancando en puerto $PORT ..."
SOCK_ARGS=()
if [[ "$SOCK" -eq 1 && -S /var/run/docker.sock ]]; then
  SOCK_ARGS=(-v /var/run/docker.sock:/var/run/docker.sock)
fi
docker run --rm -d --name "$NAME" -p "${PORT}:${PORT}" "${SOCK_ARGS[@]}" "$IMAGE"

echo "3/3 Esperando health (hasta ~30s) ..."
OK=0
for _ in $(seq 1 15); do
  sleep 2
  for path in /_floci/health /_localstack/health /_floci-oci/health /; do
    if curl -sf "http://127.0.0.1:${PORT}${path}" >/dev/null 2>&1; then
      OK=1
      break
    fi
  done
  [[ "$OK" -eq 1 ]] && break
done

if [[ "$OK" -eq 1 ]]; then
  echo "Health OK."
else
  echo "AVISO: no se confirmó health HTTP; revisa: docker logs $NAME"
fi

echo ""
echo "=== Variables / siguientes pasos ==="
case "$CLOUD" in
  aws)
    cat <<'EOF'
export AWS_ENDPOINT_URL=http://localhost:4566
export AWS_ACCESS_KEY_ID=test AWS_SECRET_ACCESS_KEY=test AWS_DEFAULT_REGION=us-east-1
aws s3 mb s3://cloudlite-lab
echo "hola CloudLite" > hola.txt
aws s3 cp hola.txt s3://cloudlite-lab/
aws s3 ls s3://cloudlite-lab/
EOF
    if command -v aws >/dev/null 2>&1; then
      export AWS_ENDPOINT_URL=http://localhost:4566
      export AWS_ACCESS_KEY_ID=test AWS_SECRET_ACCESS_KEY=test AWS_DEFAULT_REGION=us-east-1
      echo "hola CloudLite UNIAJC" > hola-cloudlite.txt
      aws s3 mb s3://cloudlite-lab 2>/dev/null || true
      aws s3 cp hola-cloudlite.txt s3://cloudlite-lab/ 2>/dev/null || true
      aws s3 ls s3://cloudlite-lab/ || true
    fi
    ;;
  az)
    echo "BlobEndpoint=http://localhost:4577/devstoreaccount1 — ver https://floci.io/"
    ;;
  gcp)
    echo "export CLOUDSDK_API_ENDPOINT_OVERRIDES_STORAGE=http://localhost:4588/"
    echo "export CLOUDSDK_CORE_PROJECT=floci-local"
    ;;
  oci)
    echo "Endpoint OCI local: http://localhost:4599"
    ;;
esac

echo ""
echo "Detener: $0 $CLOUD --stop"
echo "Docs:    ./README.md · plan: ../PLAN_VIABILIDAD_FLOCI_2026-2.md"
