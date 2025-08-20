from fastapi import FastAPI
from app.api.routes import router
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

app = FastAPI(title="Capstone RAG Assistant")


# include routes
app.include_router(router)


@app.get("/health")
def health():
    return {"status": "ok"}