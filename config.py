import os

# LinkedIn credentials
LINKEDIN_EMAIL = ""
LINKEDIN_PASSWORD = ""

# File paths
URLS_FILE = "urls.xlsx"
LOG_FILE = "logs/linkedin_checker.log"

# Ensure logs directory exists
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
