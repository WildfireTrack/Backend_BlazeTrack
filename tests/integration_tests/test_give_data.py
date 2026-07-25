import json
from main import app
from source.api.dependencies.data_fetcher import fetch_global_widfire_data


def _mock_fetch():
    return json.dumps([{"latitude": 10.0, "longitude": 20.0}])


def test_give_data_returns_json():
    from fastapi.testclient import TestClient

    app.dependency_overrides[fetch_global_widfire_data] = _mock_fetch
    client = TestClient(app)
    response = client.get("/api/v1/")
    assert response.status_code == 200
    data = response.json()
    assert "data" in data
    app.dependency_overrides.clear()
