# Copyright 2023 Marin Pejcin


import logging
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any, Dict, Optional

import emails
from emails.template import JinjaTemplate
from jose import jwt

from config.configs import get_email_config, get_api_config, get_security_config


def send_email(
    email_to: str,
    subject_template: str = "",
    html_template: str = "",
    environment: Dict[str, Any] = {},
) -> None:
    assert get_email_config().enabled, "no provided configuration for email variables"
    message = emails.Message(
        subject=JinjaTemplate(subject_template),
        html=JinjaTemplate(html_template),
        mail_from=(get_email_config().from_name, get_email_config().from_email),
    )
    smtp_options = {"host": get_email_config().smtp_host, "port": get_email_config().smpt_port}
    if get_email_config().smtp_tls:
        smtp_options["tls"] = True
    if get_email_config().smtp_user:
        smtp_options["user"] = get_email_config().smtp_user
    if get_email_config().smtp_password:
        smtp_options["password"] = get_email_config().smtp_password
    response = message.send(to=email_to, render=environment, smtp=smtp_options)
    logging.info(f"send email result: {response}")


def send_test_email(email_to: str) -> None:
    project_name = get_api_config().project_name
    subject = f"{project_name} - Test email"
    with open(Path(get_email_config().templates_dir) / "test_email.html") as f:
        template_str = f.read()
    send_email(
        email_to=email_to,
        subject_template=subject,
        html_template=template_str,
        environment={"project_name": get_api_config().project_name, "email": email_to},
    )


def send_reset_password_email(email_to: str, email: str, token: str) -> None:
    project_name = get_api_config().project_name
    subject = f"{project_name} - Password recovery for user {email}"
    with open(Path(get_email_config().templates_dir) / "reset_password.html") as f:
        template_str = f.read()
    server_host = get_api_config().host
    link = f"{server_host}/reset-password?token={token}"
    send_email(
        email_to=email_to,
        subject_template=subject,
        html_template=template_str,
        environment={
            "project_name": get_api_config().project_name,
            "username": email,
            "email": email_to,
            "valid_hours": get_email_config().reset_token_exire_hours,
            "link": link,
        },
    )


def send_new_account_email(email_to: str, username: str) -> None:
    project_name = get_api_config().project_name
    subject = f"{project_name} - New account for user {username}"
    with open(Path(get_email_config().templates_dir) / "new_account.html") as f:
        template_str = f.read()
    link = get_api_config().host
    send_email(
        email_to=email_to,
        subject_template=subject,
        html_template=template_str,
        environment={
            "project_name": get_api_config().project_name,
            "username": username,
            "email": email_to,
            "link": link,
        },
    )


def generate_password_reset_token(email: str) -> str:
    delta = timedelta(hours=get_email_config().reset_token_exire_hours)
    now = datetime.utcnow()
    expires = now + delta
    exp = expires.timestamp()
    encoded_jwt = jwt.encode(
        {"exp": exp, "nbf": now, "sub": email}, get_security_config().secret_key, algorithm="HS256",
    )
    return encoded_jwt


def verify_password_reset_token(token: str) -> Optional[str]:
    try:
        decoded_token = jwt.decode(token, get_security_config().secret_key, algorithms=["HS256"])
        return decoded_token["email"]
    except jwt.JWTError:
        return None