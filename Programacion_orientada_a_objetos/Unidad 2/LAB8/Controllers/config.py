"""PostgreSQL settings. Environment variables override the local defaults."""

import os


DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "user": os.getenv("DB_USER", "postgres"),
    "password": os.getenv("DB_PASSWORD", ""),
    "dbname": os.getenv("DB_NAME", "login_mvc"),
    "port": int(os.getenv("DB_PORT", "5432")),
}
