from typing import Any

from fastapi import APIRouter, Depends

from src.api.deps import get_current_user
from src.core.app import marco_polo
from src.schemas.app import AppOut, AppIn, AppArrayRangeIn, AppArrayRangeOut

router = APIRouter()


@router.post("/marcoPolo", dependencies=[Depends(get_current_user)], response_model=AppOut, status_code=200)
async def marco_polo_endpoint(
        *,
        value_in: AppIn,
) -> Any:
    result = marco_polo(value_in.value)[0]
    return AppOut(result=result)


@router.post("/marcoPoloArray", dependencies=[Depends(get_current_user)], response_model=AppArrayRangeOut, status_code=200)
async def marco_polo_array_endpoint(
        *,
        value_in: AppArrayRangeIn,
) -> Any:

    result = [marco_polo(value)[0] for value in value_in.values_array]
    return AppArrayRangeOut(result_list=result)


@router.post("/marcoPoloRange", dependencies=[Depends(get_current_user)], response_model=AppArrayRangeOut, status_code=200)
async def marco_polo_range_endpoint(
        *,
        value_in: AppArrayRangeIn,
) -> Any:

    result = [marco_polo(value)[0] for value in range(value_in.values_array[0], value_in.values_array[1] + 1)]
    return AppArrayRangeOut(result_list=result)
