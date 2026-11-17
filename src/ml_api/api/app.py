from fastapi import FastAPI, HTTPException
from ml_api.api.schemas import PredictInput, PredictResponse
from ml_api.Model.predictor import RideDuration

app = FastAPI()
model = RideDuration()

@app.post('/predict', response_model=PredictResponse)
async def post_prediction(prediction: PredictInput):
  result = model.predict([prediction.distance_km, prediction.passengers])
  return PredictResponse(duration_min=round(result,2))

@app.get('/feedback')
async def get_feedback():
  return{"feedback": "The model is great!"}

@app.get('/health')
async def get_health():
  return {"status": "healthy"}