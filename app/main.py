from fastapi import FastAPI

app = FastAPI()


# first block
from transformers import pipeline
sentiment_model = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english")


from pydantic import BaseModel

class PredictionRequest(BaseModel):
  query_string: str


@app.get("/health")
def health():
    return "Service is online."


@app.post("/prediction")
def my_endpoint(request: PredictionRequest):
    return sentiment_model(request.query_string)
  
