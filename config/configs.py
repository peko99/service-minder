# Copyright 2023 Marin Pejcin


from functools import lru_cache

from config import api, database, security, email


@lru_cache()
def get_api_config():
    return api.config


@lru_cache()
def get_database_config():
    return database.config


@lru_cache()
def get_security_config():
    return security.config


@lru_cache()
def get_email_config():
    return email.config
