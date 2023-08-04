from pydantic import BaseModel
from typing import Union


class ExceptionResponse(BaseModel):
    message: str
    success: bool = False
    status_code: int
    path: str
    detail: Union[str, None] = None
