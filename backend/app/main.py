import os
import asyncio
import logging
from pathlib import Path
from typing import Optional

from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from pydantic_settings import BaseSettings
from fastapi import Depends
from sqlalchemy.orm import Session
from app.db import SessionLocal
from app.config import settings


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s — %(message)s",
)
logger = logging.getLogger("backend")

UPLOAD_DIR = Path(__file__).resolve().parent.parent / "data" / "uploads"
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

app = FastAPI(title=settings.app_name)

# CORS for local frontend dev (Vite runs on 5173 by default)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[o.strip() for o in settings.allowed_origins.split(",") if o.strip()],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatRequest(BaseModel):
    message: str
    user: Optional[str] = "local"


@app.get("/health")
async def health():
    return {
        "status": "ok",
        "app": settings.app_name,
        "env": settings.environment,
        "commit": os.getenv("COMMIT_SHA", "dev"),
    }


@app.post("/chat")
async def chat(req: ChatRequest):
    """SSE streaming stub — integrates RAG on Day 5."""
    async def token_stream():
        demo = "Hello! This is your Day‑2 chat stub. RAG arrives on Day 5."
        for token in demo.split(" "):
            yield f"data: {token} "
            yield ""
            await asyncio.sleep(0.03)
            yield "data: [DONE]"

    return StreamingResponse(token_stream(), media_type="text/event-stream")


@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    """Accept PDF/CSV; save locally for now."""
    allowed = {
        "application/pdf",
        "text/csv",
        "application/vnd.ms-excel",
        "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        "text/plain",
    }
    if file.content_type not in allowed:
        raise HTTPException(status_code=415, detail=f"Unsupported file type: {file.content_type}")

    dest = UPLOAD_DIR / file.filename
    contents = await file.read()
    with dest.open("wb") as f:
        f.write(contents)

    logger.info("Saved upload %s (%d bytes)", file.filename, dest.stat().st_size)
    return {"ok": True, "filename": file.filename, "bytes": dest.stat().st_size}


@app.post("/ingest")
async def ingest():
    """Stub endpoint — we wire real ingestion on Day 4."""
    return {"ok": True, "message": "Ingestion queued (stub). Implement on Day 4."}


@app.get("/docs")
async def docs_list():
    files = [p.name for p in UPLOAD_DIR.glob("*") if p.is_file()]
    return {"count": len(files), "files": files}


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

from sqlalchemy import text

@app.get("/db-check")
async def db_check(db: Session = Depends(get_db)):
    result = db.execute(
        text("SELECT table_name FROM information_schema.tables WHERE table_schema='public';")
    ).fetchall()
    tables = [row[0] for row in result]  # Extract table names from each row
    return {"ok": True, "tables": tables}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)