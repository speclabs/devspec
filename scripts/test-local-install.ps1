param(
    [string]$Profile = "all"
)

$ErrorActionPreference = "Stop"

$Root = Resolve-Path (Join-Path $PSScriptRoot "..")
if (-not $env:UV_CACHE_DIR) {
    $env:UV_CACHE_DIR = Join-Path $Root ".uv-cache"
}
$TempRoot = Join-Path ([System.IO.Path]::GetTempPath()) ("devspec-local-install-" + [System.Guid]::NewGuid().ToString("N"))
New-Item -ItemType Directory -Path $TempRoot | Out-Null
$Pushed = $false

function Invoke-Checked {
    param(
        [Parameter(Mandatory = $true)]
        [string]$FilePath,
        [Parameter(ValueFromRemainingArguments = $true)]
        [string[]]$Arguments
    )

    & $FilePath @Arguments
    if ($LASTEXITCODE -ne 0) {
        throw "Command failed with exit code ${LASTEXITCODE}: $FilePath $($Arguments -join ' ')"
    }
}

try {
    Push-Location $Root
    $Pushed = $true
    Invoke-Checked uv run devspec version
    Invoke-Checked uv run devspec init --target $TempRoot --profile $Profile --repo-state existing
    Invoke-Checked uv run devspec doctor --target $TempRoot --profile $Profile
    Invoke-Checked uv run devspec diff --target $TempRoot --profile $Profile
    Invoke-Checked uv run devspec sync --target $TempRoot --profile $Profile --dry-run
    Pop-Location
    $Pushed = $false
    Write-Host "devspec local install smoke test passed: $TempRoot"
}
finally {
    if ($Pushed) {
        Pop-Location
    }
    if (Test-Path $TempRoot) {
        Remove-Item -LiteralPath $TempRoot -Recurse -Force
    }
}
