$ErrorLocalPreference = "Stop"

if (!(Test-Path(.\.venv\Scripts\Activate.ps1))) {
    Write-Host "Virtual environment not found. Creating a new one..."
    python -m venv .venv
}

.\.venv\Scripts\Activate.ps1
python app\main.py
