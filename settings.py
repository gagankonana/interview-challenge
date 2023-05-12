import os
from dotenv import load_dotenv

load_dotenv()


def get_env(variable_name, default=None):
    value = os.getenv(variable_name, default)
    if value and str(value).lower() in ("true", "false"):
        return str(value).lower() == "true"
    return value


# Postgres
DB_HOST = get_env("DB_HOST", "localhost")
DB_NAME = get_env("DB_NAME", "dbname")
DB_USER = get_env("DB_USER", "user")
DB_PASSWORD = get_env("DB_PWD", "password")

DB_URL: str = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
