from fastapi import APIRouter


router = APIRouter()


@router.post("/chat")
def chat():
    return {"message": "chat endpoint stub"}


@router.post("/upload")
def upload():
    return {"message": "upload endpoint stub"}


@router.post("/ingest")
def ingest():
    return {"message": "ingest endpoint stub"}


@router.get("/docs")
def list_docs():
    return {"docs": []}