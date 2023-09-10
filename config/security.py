# Copyright 2023 Marin Pejcin


from pydantic_settings import BaseSettings


class SecurityConfig(BaseSettings):
    access_token_expiration_minutes: int = 60*24*8
    secret_key: str

    class Config:
        env_prefix = "security_"
        env_file = ".env"


config = SecurityConfig()