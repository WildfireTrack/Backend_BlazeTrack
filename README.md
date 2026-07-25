# BlazeTrack Backend

A FastAPI backend that proxies global wildfire hotspot data from the [NASA FIRMS](https://firms.modaps.eosdis.nasa.gov/) (Fire Information for Resource Management System) API and serves it as JSON.

## Tech Stack

- **Python** 3.12
- **FastAPI** with Uvicorn
- **Pandas** for CSV parsing
- **uv** package manager

## Project Structure

```
Backend_BlazeTrack/
├── main.py                     # FastAPI app entry point
├── source/
│   ├── config/settings/        # App configuration (env vars, constants)
│   ├── api/
│   │   ├── routes/             # API route handlers
│   │   └── dependencies/       # Data fetcher (NASA FIRMS client)
│   ├── models/                 # Schemas and DB models (WIP)
│   └── utils/                  # Utility modules (WIP)
├── tests/
│   ├── unit_tests/
│   ├── integration_tests/
│   └── end_to_end_tests/
├── .env                        # Environment variables (not committed)
└── pyproject.toml
```

## Getting Started

### Prerequisites

- Python >= 3.11
- [uv](https://docs.astral.sh/uv/) package manager
- A [NASA FIRMS API key](https://firms.modaps.eosdis.nasa.gov/api/area/)

### Installation

```bash
# Clone the repo
git clone <repo-url>
cd Backend_BlazeTrack

# Install dependencies
uv sync
```

### Configuration

Create a `.env` file in the project root:

```env
MAP_KEY=your_nasa_firms_api_key
ALLOWED_ORIGINS=["http://localhost:3000"]
ALLOW_CREDENTIALS=true
ALLOW_METHODS=["*"]
ALLOW_HEADERS=["*"]
```

### Running the Server

```bash
uv run uvicorn main:app --reload
```

The server starts at `http://localhost:8000`.

### Running Tests

```bash
uv run pytest
```

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | `/` | Welcome message |
| GET | `/api/v1/` | Fetch global wildfire hotspot data |
| GET | `/docs` | Swagger UI documentation |
| GET | `/openapi.json` | OpenAPI schema |

### Response Format

`GET /api/v1/` returns:

```json
{
  "data": [
    {
      "latitude": 40.7128,
      "longitude": -74.006,
      "brightness": 301.2,
      "scan": 1.0,
      "track": 1.0,
      "acq_date": "2026-07-25",
      ...
    }
  ]
}
```

Data is sourced from the **VIIRS NOAA-20 NRT** satellite feed.
