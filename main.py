# Copyright 2023 Marin Pejcin

import uvicorn

from app import app
from config.configs import get_api_config


def main():
    uvicorn.run(app, host=get_api_config().host, port=get_api_config().port)


if __name__ == "__main__":
    main()