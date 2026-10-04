# Mobile Backend API

Initial project structure for the mobile application's backend API.

## Project structure

```text
.
+-- src/
|   `-- app/
|       |-- __init__.py
|       `-- items.py
+-- tests/
+-- data/
+-- requirements.txt
`-- pyproject.toml
```

The application source is intentionally kept as a scaffold. API routes and
business logic can be added under `src/app/`.

## Setup

Create and activate a virtual environment, then install the dependencies:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Alternatively, install the package with its development dependencies:

```powershell
python -m pip install -e ".[dev]"
```

## Testing

Run the test suite with:

```powershell
pytest
```

## Running the API

Once an ASGI application is added to `src/app/`, run it with:

```powershell
uvicorn app.main:app --reload
```