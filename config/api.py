# Copyright 2023 Marin Pejcin


from pydantic import BaseSettings


class APIConfig(BaseSettings):
    host: str = "localhost"
    port: int = 5000

    class Config:
        env_prefix = "api_"
        env_file = ".env"


config = APIConfig()
