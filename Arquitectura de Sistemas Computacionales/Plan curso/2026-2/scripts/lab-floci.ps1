#Requires -Version 5.1
<#
.SYNOPSIS
  MVP UNIAJC — arranca Floci (emulador cloud local) para el lab CloudLite.
.DESCRIPTION
  Sin cuenta cloud ni tarjeta. Requiere Docker en ejecución.
  Variantes: aws (floci), az (floci-az), gcp (floci-gcp), oci (floci-oci).
.PARAMETER Cloud
  aws | az | gcp | oci  (default: aws)
.PARAMETER Stop
  Detiene y elimina el contenedor del lab.
.EXAMPLE
  .\lab-floci.ps1 -Cloud aws
#>
[CmdletBinding()]
param(
    [ValidateSet('aws', 'az', 'gcp', 'oci')]
    [string]$Cloud = 'aws',
    [switch]$Stop
)

$ErrorActionPreference = 'Stop'

$map = @{
    aws = @{ Image = 'floci/floci:latest';     Port = 4566; Name = 'uniajc-floci-aws'; Sock = $true }
    az  = @{ Image = 'floci/floci-az:latest';  Port = 4577; Name = 'uniajc-floci-az';  Sock = $false }
    gcp = @{ Image = 'floci/floci-gcp:latest'; Port = 4588; Name = 'uniajc-floci-gcp'; Sock = $false }
    oci = @{ Image = 'floci/floci-oci:latest'; Port = 4599; Name = 'uniajc-floci-oci'; Sock = $true }
}

$cfg = $map[$Cloud]
Write-Host ""
Write-Host "UNIAJC · CloudLite · Lab Floci ($Cloud)" -ForegroundColor Cyan
Write-Host "Emulador local · MIT · sin cuenta · sin tarjeta" -ForegroundColor DarkGray
Write-Host ""

function Test-Docker {
    try {
        docker info 1>$null 2>$null
        return $LASTEXITCODE -eq 0
    } catch {
        return $false
    }
}

if (-not (Test-Docker)) {
    Write-Host "ERROR: Docker no responde." -ForegroundColor Red
    Write-Host "Opciones:" -ForegroundColor Yellow
    Write-Host "  1) Abre Docker Desktop y vuelve a ejecutar este script."
    Write-Host "  2) Camino navegador: LabEx Docker Playground / Killercoda (ver README.md)."
    exit 1
}

if ($Stop) {
    Write-Host "Deteniendo $($cfg.Name)..."
    docker rm -f $cfg.Name 2>$null | Out-Null
    Write-Host "Listo."
    exit 0
}

$existing = docker ps -a --filter "name=^/$($cfg.Name)$" --format '{{.Names}}' 2>$null
if ($existing) {
    Write-Host "Contenedor existente: $($cfg.Name) — reiniciando..."
    docker rm -f $cfg.Name 2>$null | Out-Null
}

Write-Host "1/3 Pull $($cfg.Image) ..."
docker pull $cfg.Image
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

Write-Host "2/3 Arrancando en puerto $($cfg.Port) ..."
$runArgs = @(
    'run', '--rm', '-d',
    '--name', $cfg.Name,
    '-p', "$($cfg.Port):$($cfg.Port)"
)
if ($cfg.Sock) {
    # Lambda / Functions / sidecars (si Docker Desktop lo expone)
    if (Test-Path '\\.\pipe\docker_engine') {
        # Windows named pipe: omit bind típico de Linux; imagen aún sirve APIs in-process
    } elseif (Test-Path '/var/run/docker.sock') {
        $runArgs += @('-v', '/var/run/docker.sock:/var/run/docker.sock')
    }
}
$runArgs += $cfg.Image
& docker @runArgs
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

Write-Host "3/3 Esperando health (hasta ~30s) ..."
$ok = $false
foreach ($i in 1..15) {
    Start-Sleep -Seconds 2
    try {
        $urls = @(
            "http://127.0.0.1:$($cfg.Port)/_floci/health",
            "http://127.0.0.1:$($cfg.Port)/_localstack/health",
            "http://127.0.0.1:$($cfg.Port)/_floci-oci/health",
            "http://127.0.0.1:$($cfg.Port)/"
        )
        foreach ($u in $urls) {
            try {
                $r = Invoke-WebRequest -Uri $u -UseBasicParsing -TimeoutSec 2
                if ($r.StatusCode -ge 200 -and $r.StatusCode -lt 500) {
                    $ok = $true
                    break
                }
            } catch { }
        }
    } catch { }
    if ($ok) { break }
}

if ($ok) {
    Write-Host "Health OK." -ForegroundColor Green
} else {
    Write-Host "AVISO: no se confirmó health HTTP; revisa: docker logs $($cfg.Name)" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "=== Variables / siguientes pasos ===" -ForegroundColor Cyan
switch ($Cloud) {
    'aws' {
        Write-Host '$env:AWS_ENDPOINT_URL="http://localhost:4566"'
        Write-Host '$env:AWS_ACCESS_KEY_ID="test"; $env:AWS_SECRET_ACCESS_KEY="test"; $env:AWS_DEFAULT_REGION="us-east-1"'
        Write-Host 'aws s3 mb s3://cloudlite-lab'
        Write-Host 'aws s3 cp .\hola.txt s3://cloudlite-lab/'
        if (Get-Command aws -ErrorAction SilentlyContinue) {
            $env:AWS_ENDPOINT_URL = 'http://localhost:4566'
            $env:AWS_ACCESS_KEY_ID = 'test'
            $env:AWS_SECRET_ACCESS_KEY = 'test'
            $env:AWS_DEFAULT_REGION = 'us-east-1'
            "hola CloudLite UNIAJC" | Out-File -Encoding utf8 hola-cloudlite.txt
            aws s3 mb s3://cloudlite-lab 2>$null
            aws s3 cp hola-cloudlite.txt s3://cloudlite-lab/ 2>$null
            aws s3 ls s3://cloudlite-lab/
        }
    }
    'az' {
        Write-Host 'AZURE_STORAGE_CONNECTION_STRING con BlobEndpoint=http://localhost:4577/devstoreaccount1'
        Write-Host 'Ver quick start: https://floci.io/'
    }
    'gcp' {
        Write-Host '$env:CLOUDSDK_API_ENDPOINT_OVERRIDES_STORAGE="http://localhost:4588/"'
        Write-Host '$env:CLOUDSDK_CORE_PROJECT="floci-local"'
    }
    'oci' {
        Write-Host 'Endpoint OCI local: http://localhost:4599'
        Write-Host 'floci oci setup  (si tienes floci-cli) + oci os bucket create ...'
    }
}

Write-Host ""
Write-Host "Detener: .\lab-floci.ps1 -Cloud $Cloud -Stop" -ForegroundColor DarkGray
Write-Host "Docs:    .\README.md · plan: ..\PLAN_VIABILIDAD_FLOCI_2026-2.md" -ForegroundColor DarkGray
