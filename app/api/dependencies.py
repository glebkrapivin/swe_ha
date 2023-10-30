from functools import lru_cache

from app.db.repositories.knowledge_base import MemoryKnowledgeBaseRepository
from app.transformers.fake import FakeTransformer


# easiest hack for a singleton here
@lru_cache()
def get_memory_repository():
    repo = MemoryKnowledgeBaseRepository(transformer=FakeTransformer())
    return repo
