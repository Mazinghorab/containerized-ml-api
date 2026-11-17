from fastapi.testclient import TestClient
from ml_api.api.schemas import PredictInput, PredictResponse
from ml_api.api.app import app

client = TestClient(app)

def test_predict_endpoint_success():
  response = client.post(
    "/predict",
    json={"distance_km": 5.0, "passengers": 1}
  )
  assert response.status_code == 200
  assert "duration_min" in response.json()
  assert isinstance(response.json()["duration_min"], float)

def test_predict_endpoint_validation_error():
  response = client.post(
    "/predict",
    json={"passengers": 1}
  )
  assert response.status_code == 422