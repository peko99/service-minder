# Copyright 2023 Marin Pejcin


from functools import lru_cache

from config import api


@lru_cache()
def get_api_config():
    return api.config
