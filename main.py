import logging

from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from app.campaign.campaign_router import campaign_router
from context.shared.domain.constants.error_constants import ErrorConstants
from context.shared.domain.exceptions.base_exception import BaseException
from context.shared.domain.responses.exception_response import ExceptionResponse
from config import Settings

settings = Settings()

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    responses={
        status.HTTP_422_UNPROCESSABLE_ENTITY: {'model': ExceptionResponse},
    }
)

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s (%(asctime)s): [%(name)s][%(funcName)s] %(message)s (Line: %(lineno)d [%(filename)s])"
)


@app.exception_handler(BaseException)
def exception_base_handler(request: Request, exc: BaseException):
    response = ExceptionResponse(message=exc.detail, status_code=exc.status_code, path=str(request.url))
    return JSONResponse(status_code=exc.status_code, content=jsonable_encoder(response))


@app.exception_handler(RequestValidationError)
def request_exception_handler(request: Request, exc: Exception):
    response = ExceptionResponse(message=ErrorConstants.BAD_REQUEST_ERROR, detail=str(exc), status_code=422,
                                 path=str(request.url))
    return JSONResponse(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, content=jsonable_encoder(response))


@app.exception_handler(Exception)
def request_exception_handler(request: Request, exc: Exception):
    response = ExceptionResponse(message=ErrorConstants.INTERNAL_SERVER_ERROR, detail=str(exc), status_code=500,
                                 path=str(request.url))
    return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content=jsonable_encoder(response))


app.include_router(campaign_router)
