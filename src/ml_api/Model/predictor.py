from typing import Optional, Protocol

class Estimator(Protocol):
  def predict(self, features: list[float]) -> list[float]: ...

class _HeuristicEstimator:
  #: Assumed average speed in km per minute (~30 km/h).
  AVG_SPEED_KM_PER_MIN = 0.5
  #: Extra minutes added per passenger (boarding overhead).
  PASSENGER_OVERHEAD_MIN = 0.5

  def predict(self, features: list[float]) -> list[float]:
    distance, passengers = features[0], features[1]
    duration = distance / self.AVG_SPEED_KM_PER_MIN
    duration += passengers * self.PASSENGER_OVERHEAD_MIN
    return [round(duration, 2)]

class RideDuration:
  def __init__(self, threshold: Optional[float] = None) -> None:
    self._model: Estimator = _HeuristicEstimator()
    self.threshold = threshold

  def predict(self, features: list[float]) -> float:
    duration = float(self._model.predict(features)[0])
    if self.threshold is not None:
      duration = min(duration, self.threshold)
    return duration