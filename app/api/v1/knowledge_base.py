from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from starlette.status import HTTP_204_NO_CONTENT

from app.api.dependencies import get_memory_repository
from app.schemas.knowledge_base import DocumentCreateRequest, DocumentCreateResponse, KnowledgeBaseCreateResponse, \
    SimilarSearchResponse, SimilarSearchRequest

router = APIRouter()


@router.post("/", response_model=KnowledgeBaseCreateResponse)
def create_knowledge_base(kb_repo=Depends(get_memory_repository)):
    kb_id = kb_repo.create()
    return KnowledgeBaseCreateResponse(id=str(kb_id))


@router.delete('/{kb_id}', status_code=HTTP_204_NO_CONTENT)
def delete_knowledge_base(kb_id: UUID, kb_repo=Depends(get_memory_repository)):
    try:
        kb_repo.delete(kb_id)
    except ValueError:
        raise HTTPException(status_code=404)


@router.post("/{kb_id}/document")
def add_document_to_knowledge_base(kb_id: UUID, request: DocumentCreateRequest,
                                   kb_repo=Depends(get_memory_repository)):
    try:
        doc_id = kb_repo.add_document(kb_id, request.text)
    except ValueError:
        raise HTTPException(status_code=404)

    # pydantic validates that it is not empty
    return DocumentCreateResponse(id=doc_id)


@router.delete("/{kb_id}/document/{doc_id}", status_code=HTTP_204_NO_CONTENT)
def del_document_from_knowledge_base(kb_id: UUID, doc_id: str, kb_repo=Depends(get_memory_repository)):
    try:
        kb_repo.delete_document(kb_id, doc_id)
    except ValueError:
        raise HTTPException(status_code=404)


@router.post("/{kb_id}/similar", response_model=SimilarSearchResponse)
def get_similar_docs(kb_id: UUID, request: SimilarSearchRequest, kb_repo=Depends(get_memory_repository)):
    if request.n_similar < 1:
        raise HTTPException(status_code=400)

    docs_n_scores = kb_repo.get_similar(kb_id, request.text, request.n_similar)
    res = []
    for item in docs_n_scores:
        d = SimilarSearchResponse.Document(text=item.get("text", ""), score=item.get('score', 0.0))
        res.append(d)
    return SimilarSearchResponse(documents=res)
