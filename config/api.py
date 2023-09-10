# Copyright 2023 Marin Pejcin


from pydantic_settings import BaseSettings


class APIConfig(BaseSettings):
    project_name: str = "ServiceMinder"
    host: str = "localhost"
    port: int = 5000

    class Config:
        env_prefix = "api_"
        env_file = ".env"


config = APIConfig()
