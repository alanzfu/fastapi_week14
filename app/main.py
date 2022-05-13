from fastapi import FastAPI

app = FastAPI()


# first block
from transformers import pipeline
sentiment_model = pipeline("sentiment-analysis")

# from transformers import AutoTokenizer, AutoModel

# >>> tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
# >>> model = AutoModel.from_pretrained("bert-base-uncased")


# second block
from pydantic import BaseModel

class PredictionRequest(BaseModel):
  query_string: str


@app.get("/health")
def health():
    return "Service is online."


@app.post("/prediction")
def my_endpoint(request: PredictionRequest):
    return sentiment_model(request.query_string)
  
