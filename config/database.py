# Copyright 2023 Marin Pejcin


from pydantic_settings import BaseSettings


class DatabaseConfig(BaseSettings):
    user: str = ""
    password: str = ""
    host: str = "host"
    port: str = "5432"
    database: str = "service_minder"

    class Config:
        env_prefix = "pg_"
        env_file = ".env"


config = DatabaseConfig()