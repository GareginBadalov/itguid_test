from typing import Any

from fastapi import APIRouter, HTTPException
from starlette.responses import JSONResponse


from src.core.auth import authenticate, AuthenticationError, UserNotFoundException
from src.core.security import create_access_token, create_refresh_token
from src.schemas.user import UserLoginIn, UserLoginOut

router = APIRouter()


@router.post("/login", response_model=UserLoginOut, status_code=200)
async def login(
        *,
        user_in: UserLoginIn,
) -> Any:
    try:
        user = await authenticate(email=user_in.email, password=user_in.password)

        return JSONResponse(
            content={
                "access_token": create_access_token(user_id=user["id"]),
                "refresh_token": create_refresh_token(user_id=user["id"]),
            },
        )
    except (AuthenticationError, UserNotFoundException) as ex:
        raise HTTPException(status_code=400, detail={ex.error_code: ex.message})
