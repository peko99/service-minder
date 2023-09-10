# Copyright 2023 Marin Pejcin


from ast import Dict
import secrets
from typing import Any, Optional
from pydantic import EmailStr, validator
from pydantic_settings import BaseSettings


class EmailConfig(BaseSettings):
    smtp_tls: bool = True
    smpt_port: Optional[int] = 587
    smtp_host: Optional[str] = None
    smtp_user: Optional[str] = None
    smtp_password: Optional[str] = None
    from_email: Optional[EmailStr] = None
    from_name: Optional[str] = "Admin"
    reset_token_exire_hours: int = 48
    templates_dir: str = "app/email_templates/build"
    enabled: bool = True
    test_user: EmailStr = "test@example.com"


    # @validator("EMAILS_ENABLED", pre=True)
    # def get_emails_enabled(cls, v: bool, values: Dict[str, Any]) -> bool:
    #     return bool(
    #         values.get("SMTP_HOST")
    #         and values.get("SMTP_PORT")
    #         and values.get("EMAILS_FROM_EMAIL")
    #     )

    class Config:
        env_prefix = "emails_"
        env_file = ".env"


config = EmailConfig()