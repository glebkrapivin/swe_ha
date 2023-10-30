import uuid
from typing import List

from pydantic import BaseModel


class DocumentCreateRequest(BaseModel):
    text: str


class DocumentCreateResponse(BaseModel):
    id: str


class KnowledgeBaseCreateResponse(BaseModel):
    id: str


class KnowledgeBaseCreateRequest(BaseModel):
    pass


class SimilarSearchRequest(BaseModel):
    text: str
    n_similar: int


class SimilarSearchResponse(BaseModel):
    class Document(BaseModel):
        text: str
        score: float

    documents: List[Document]
