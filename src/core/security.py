from datetime import datetime, timedelta

from jose import jwt
from passlib.context import CryptContext

from src.config import SECRET_AUTH, ALGORITHM, SECRET_REFRESH, access_token_expire_minutes, \
    refresh_token_expire_minutes, SECRET_VERIFY

PWD_CONTEXT = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return PWD_CONTEXT.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return PWD_CONTEXT.hash(password)


def create_access_token(user_id: int) -> str:
    expire = datetime.utcnow() + timedelta(
        minutes=access_token_expire_minutes
    )
    to_encode = {'exp': expire, 'sub': str(user_id)}
    encoded_jwt = jwt.encode(to_encode, SECRET_AUTH,
                             algorithm=ALGORITHM)
    return encoded_jwt


def create_verify_token(email: str) -> str:
    expire = datetime.utcnow() + timedelta(
        minutes=access_token_expire_minutes
    )
    to_encode = {'exp': expire, 'mail': email}
    encoded_jwt = jwt.encode(to_encode, SECRET_VERIFY,
                             algorithm=ALGORITHM)
    return encoded_jwt


def create_refresh_token(user_id: int) -> str:
    expire = datetime.utcnow() + timedelta(
        minutes=refresh_token_expire_minutes
    )
    to_encode = {'exp': expire, 'sub': str(user_id)}
    encoded_jwt = jwt.encode(to_encode, SECRET_REFRESH,
                             algorithm=ALGORITHM)
    return encoded_jwt
