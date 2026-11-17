import pytest
from unittest.mock import MagicMock
from ml_api.Model.predictor import RideDuration

def test_predict_returns_float():
  model = RideDuration()
  model._model = MagicMock()
  model._model.predict.return_value = [23.5]
  result = model.predict([5.0, 1])
  assert isinstance(result, float)
  assert result == 23.5

@pytest.mark.parametrize(
  "distance,pax,expected",
  [
    (1.0, 1, 5.2),
    (10.0, 2, 24.8),
    (0.5, 4, 3.1)
  ],
)
def test_predict_multiple_input(distance, pax, expected):
  model = RideDuration()
  model._model = MagicMock()
  model._model.predict.return_value = [expected]
  assert model.predict([distance, pax]) == expected

@pytest.fixture
def mock_model():
  model = RideDuration()
  model._model = MagicMock()
  model._model.predict.return_value = [15.0]
  return model

def test_threshold_clipping(mock_model):
  mock_model.threshold = 10.0
  result = mock_model.predict([100.0, 1])
  assert result == 10.0