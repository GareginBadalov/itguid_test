from pathlib import Path
from typing import List

from dotenv import load_dotenv
import os


load_dotenv()

SECRET_AUTH = os.environ.get("SECRET_AUTH")
SECRET_REFRESH = os.environ.get("SECRET_REFRESH")
SECRET_VERIFY = os.environ.get("SECRET_VERIFY")
ALGORITHM = os.environ.get("ALGORITHM")
project_name = "ItGuild"
access_token_expire_minutes: int = 60
refresh_token_expire_minutes: int = 60 * 24 * 30
api_v1_path: str = "/api/v1"
backend_cors_origins: List[str] = ["*"]
mail_verify_front_end_url = "http://80.90.191.125:3000/registration-confirmation?token="
