from typing import List, Union
from pydantic import BaseModel


class AppIn(BaseModel):
    value: int

    class Config:
        orm_mode = True


class AppArrayRangeIn(BaseModel):
    values_array: List[int]

    class Config:
        orm_mode = True


class AppOut(BaseModel):
    result: int | str

    class Config:
        orm_mode = True


class AppArrayRangeOut(BaseModel):
    result_list: List[int | str]
