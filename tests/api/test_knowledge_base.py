import uuid

import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


class TestV1KnowledgeBaseAPI:
    @pytest.fixture
    def create_knowledge_base(self):
        response = client.post('/api/knowledge_base/')
        assert response.status_code == 200
        kb_id = response.json()["id"]
        yield kb_id
        # Clean up after the test
        try:
            client.delete(f"/knowledge_base/{kb_id}")
        except:
            pass

    def test_create_knowledge_base(self):
        response = client.post("/api/knowledge_base/")
        assert response.status_code == 200
        kb_id = response.json()["id"]
        assert kb_id

    def test_delete_knowledge_base(self, create_knowledge_base):
        kb_id = create_knowledge_base

        response = client.delete(f"/api/knowledge_base/{kb_id}")
        assert response.status_code == 204

    def test_delete_non_existing_knowledge_base(self):
        response = client.delete(f"/api/knowledge_base/{str(uuid.uuid4())}")
        assert response.status_code == 404

    def test_add_document_to_knowledge_base(self, create_knowledge_base):
        kb_id = create_knowledge_base
        response = client.post(f"/api/knowledge_base/{kb_id}/document", json={"text": "Test document"})
        assert response.status_code == 200
        doc_id = response.json()["id"]
        assert doc_id

    def test_del_document_from_knowledge_base(self, create_knowledge_base):
        kb_id = create_knowledge_base
        response = client.post(f"/api/knowledge_base/{kb_id}/document", json={"text": "Test document"})
        doc_id = response.json()["id"]
        response = client.delete(f"/api/knowledge_base/{kb_id}/document/{doc_id}")
        assert response.status_code == 204

    def test_del_non_existing_document_from_knowledge_base(self, create_knowledge_base):
        kb_id = create_knowledge_base
        response = client.delete(f"/api/knowledge_base/{kb_id}/document/{str(uuid.uuid4())}")
        assert response.status_code == 404

    def test_get_similar_docs(self, create_knowledge_base):
        kb_id = create_knowledge_base
        _ = client.post(f"/api/knowledge_base/{kb_id}/document", json={"text": "Test document"})
        response = client.post(f"/api/knowledge_base/{kb_id}/similar", json={"text": "Test text", "n_similar": 1})
        assert response.status_code == 200
        data = response.json()
        assert "documents" in data
        assert len(data["documents"]) == 1
