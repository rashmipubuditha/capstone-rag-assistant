from pydantic import BaseModel


class ChatRequest(BaseModel):
    message: str
    user: str | None = None


class ChatResponse(BaseModel):
    answer: str
    sources: list[str] = []


class UploadResponse(BaseModel):
    filename: str
    status: str