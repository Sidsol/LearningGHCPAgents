# Intentionally flawed code for Lab 4 code review exercise
# This file contains hardcoded credentials — a common security mistake

# Database configuration
DATABASE_URL = "postgresql://admin:EXAMPLE_PASSWORD_HERE@prod-db.internal:5432/myapp"
DATABASE_PASSWORD = "EXAMPLE_PASSWORD_HERE"

# Third-party API keys (these are fake placeholders for the exercise)
PAYMENT_SERVICE_KEY = "pay_key_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
EMAIL_SERVICE_KEY = "email_key_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
CLOUD_ACCESS_KEY_ID = "CLOUD_KEY_ID_EXAMPLE_XXXXXXXXXXXX"
CLOUD_SECRET_ACCESS_KEY = "CLOUD_SECRET_EXAMPLE_XXXXXXXXXXXXXXXXXXXX"

# JWT configuration
JWT_SECRET = "EXAMPLE_JWT_SECRET_REPLACE_WITH_ENV_VAR"
ADMIN_PASSWORD = "admin123"

# Environment flag (should be env var)
ENVIRONMENT = "production"
DEBUG = True  # Debug mode enabled in production

# Email configuration
SMTP_HOST = "smtp.example.com"
SMTP_PORT = 587
SMTP_USERNAME = "noreply@example.com"
SMTP_PASSWORD = "EXAMPLE_SMTP_PASSWORD_HERE"


def get_database_url():
    return DATABASE_URL


def get_api_config():
    return {
        "payment_key": PAYMENT_SERVICE_KEY,
        "email_key": EMAIL_SERVICE_KEY,
        "cloud_access_key": CLOUD_ACCESS_KEY_ID,
        "cloud_secret": CLOUD_SECRET_ACCESS_KEY,
    }
