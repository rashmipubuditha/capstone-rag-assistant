from fastapi import FastAPI,Depends
from app.api.routes import router
import logging
from sqlalchemy.orm import Session
from app.db import SessionLocal


logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

app = FastAPI(title="Capstone RAG Assistant")


# include routes
app.include_router(router)


@app.get("/health")
def health():
    return {"status": "ok"}


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/db-check")
async def db_check(db: Session = Depends(get_db)):
    return {"ok": True, "tables": db.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public';").fetchall()}