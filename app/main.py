from fastapi import FastAPI
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware

from app.api.routes import router as api_router
from app.core.config import settings


# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     # init model, case it lazy loads when first called
#     # from app.db.repository.memory import MemoryKnowledgeBaseRepository
#     # x = MemoryKnowledgeBaseRepository().create()
#     # yield

def get_application() -> FastAPI:
    cors = Middleware(
        CORSMiddleware,
        allow_origins=settings.allowed_hosts,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    application = FastAPI(middleware=[cors])

    application.include_router(api_router, prefix=settings.api_prefix)

    return application


app = get_application()
