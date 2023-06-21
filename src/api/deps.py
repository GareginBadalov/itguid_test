from typing import Optional

from jose import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel

from src.config import SECRET_AUTH, api_v1_path
from src.fake_db import fake_db

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl=f'{api_v1_path}/auth/login/'
)


class TokenData(BaseModel):
    user_id: Optional[str] = None


async def get_current_user(
    token: str = Depends(oauth2_scheme),
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    payload = jwt.decode(
        token,
        SECRET_AUTH,
        algorithms=["HS256"],
        options={"verify_aud": False},
    )
    user_id: str = payload.get("sub")

    if user_id is None:
        raise credentials_exception
    token_data = TokenData(user_id=user_id)
    user = [user for user in fake_db.get("Users") if user["id"] == int(token_data.user_id)]

    if len(user) == 0:
        raise credentials_exception
    return user



