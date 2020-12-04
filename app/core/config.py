import os

PROJECT_NAME = "aurora-admin-panel"

BACKEND_VERSION = os.getenv("BACKEND_VERSION", '0.1.0')
ENVIRONMENT = os.getenv("ENVIRONMENT", "PROD")
SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
ENABLE_SENTRY = os.getenv("ENABLE_SENTRY", False)
SECRET_KEY = os.getenv("SECRET_KEY", "aurora-admin-panel")
TRAFFIC_INTERVAL = os.getenv("TRAFFIC_INTERVAL", 600)
DDNS_INTERVAL = os.getenv("DDNS_INTERVAL", 120)

API_V1_STR = "/api/v1"
