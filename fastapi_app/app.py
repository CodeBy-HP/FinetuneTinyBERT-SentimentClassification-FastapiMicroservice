import torch
import logging
import socket
from get_model import download_model_from_s3
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from transformers import AutoModelForSequenceClassification, AutoTokenizer

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

model = None
tokenizer = None
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Load model on startup and cleanup on shutdown"""
    global model, tokenizer

    try:
        logger.info("Starting model download from S3...")
        model_dir = download_model_from_s3(local_dir="./model")

        logger.info("Loading tokenizer...")
        tokenizer = AutoTokenizer.from_pretrained(model_dir)

        logger.info("Loading model...")
        model = AutoModelForSequenceClassification.from_pretrained(model_dir)
        model.to(device)
        model.eval()

        logger.info(f"Model loaded successfully on {device}")
    except Exception as e:
        logger.error(f"Error loading model: {e}")
        raise

    yield

    logger.info("Shutting down...")


app = FastAPI(title="Sentiment Analysis API", lifespan=lifespan)

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Render the home page"""
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/predict")
async def predict(request: Request, text: str = Form(...)):
    """Predict sentiment for the given text"""
    if not text.strip():
        return templates.TemplateResponse(
            "index.html",
            {"request": request, "error": "Please enter some text to analyze"},
        )

    try:
        inputs = tokenizer(
            text, return_tensors="pt", truncation=True, max_length=512, padding=True
        )
        inputs = {k: v.to(device) for k, v in inputs.items()}

        with torch.no_grad():
            outputs = model(**inputs)
            logits = outputs.logits
            probabilities = torch.nn.functional.softmax(logits, dim=-1)
            predicted_class = torch.argmax(probabilities, dim=-1).item()
            confidence = probabilities[0][predicted_class].item()

        sentiment_map = {0: "Negative", 1: "Positive"}
        sentiment = sentiment_map.get(predicted_class, "Unknown")

        return templates.TemplateResponse(
            "index.html",
            {
                "request": request,
                "text": text,
                "sentiment": sentiment,
                "confidence": round(confidence * 100, 2),
            },
        )

    except Exception as e:
        logger.error(f"Prediction error: {e}")
        return templates.TemplateResponse(
            "index.html", {"request": request, "error": f"An error occurred: {str(e)}"}
        )


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "model_loaded": model is not None,
        "device": str(device),
    }


@app.get("/container-info")
async def container_info():
    """Show which container is serving this request (useful for demo/load balancing)"""
    return {
        "container_id": socket.gethostname(),
        "status": "serving",
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
