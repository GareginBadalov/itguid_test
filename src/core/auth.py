from typing import Optional

from src.core.security import verify_password

from src.fake_db import fake_db


class UserNotFoundException(Exception):
    default_message = "Данный e-mail не зарегистрирован, пройдите регистрацию или используйте другой e-mail"
    error_code = "UserNotFound"


class AuthenticationError(Exception):
    default_message = "Введите правильный пароль"
    error_code = "AuthenticationError"


async def authenticate(
    *,
    email: str,
    password: str,
) -> Optional[dict]:
    user = [user for user in fake_db.get("Users") if user["email"] == email][0]
    if not user:
        raise UserNotFoundException
    if not verify_password(password, user["hashed_password"]):
        raise AuthenticationError
    return user
