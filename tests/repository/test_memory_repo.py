import uuid

import pytest

from app.db.repositories.knowledge_base import MemoryKnowledgeBaseRepository
from app.transformers.fake import FakeTransformer


class TestMemoryKnowledgeBaseRepository:

    @pytest.fixture
    def kb_repo(self):
        return MemoryKnowledgeBaseRepository(FakeTransformer())

    def test_create(self, kb_repo):
        kb_id = kb_repo.create()
        assert kb_id
        assert kb_id in kb_repo.data

    def test_delete(self, kb_repo):
        kb_id = kb_repo.create()
        kb_repo.delete(kb_id)
        assert kb_id not in kb_repo.data

    def test_add_document(self, kb_repo):
        kb_id = kb_repo.create()
        text = "Sample text"
        doc_id = kb_repo.add_document(kb_id, text)
        assert doc_id

    def test_delete_document(self, kb_repo):
        kb_id = kb_repo.create()
        text = "Sample text"
        doc_id = kb_repo.add_document(kb_id, text)
        kb_repo.delete_document(kb_id, doc_id)

        # did not find a method to get check that document is in store fast
        # generally, would check that the doc is no longer there
        # or that the delete function was called

    def test_get_similar(self, kb_repo):
        kb_id = kb_repo.create()
        text = "Sample text"
        _ = kb_repo.add_document(kb_id, text)
        _ = kb_repo.add_document(kb_id, text)
        similar = kb_repo.get_similar(kb_id, text, 2)
        assert len(similar) == 2
        assert "text" in similar[0]
        assert "score" in similar[0]

    def test_get_similar_kb_not_found(self, kb_repo):
        with pytest.raises(ValueError):
            kb_repo.get_similar(str(uuid.uuid4()), "Sample text", 1)

    def test_delete_non_existing_knowledge_base(self, kb_repo):
        with pytest.raises(ValueError):
            kb_repo.delete(str(uuid.uuid4()))

    def test_delete_non_existing_document(self, kb_repo):
        kb_id = kb_repo.create()
        with pytest.raises(ValueError):
            kb_repo.delete_document(kb_id, str(uuid.uuid4()))

