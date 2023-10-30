from typing import List

from pydantic import AnyHttpUrl
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    allowed_hosts: List[AnyHttpUrl] = []
    api_prefix: str = "/api"

    class Config:
        env_file = ".env"


settings = Settings()
