from fastapi import APIRouter

from app.api.v1.knowledge_base import router as kb_v1

router = APIRouter()

router.include_router(kb_v1, prefix='/knowledge_base')

