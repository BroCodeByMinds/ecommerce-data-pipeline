from fastapi.responses import JSONResponse
from typing import Any
from common.constants import Messages, ResponseStatus, StatusCodes


class ResponseBuilder:

    @staticmethod
    def success(data: Any, message: str = Messages.SUCCESS) -> JSONResponse:
        return JSONResponse(
            status_code=StatusCodes.HTTP_200_OK,
            content={
                "status": ResponseStatus.SUCCESS,
                "message": message,
                "data": data,
            }
        )

    @staticmethod
    def not_found(message: str = Messages.RESOURCE_NOT_FOUND) -> JSONResponse:
        return JSONResponse(
            status_code=StatusCodes.HTTP_404_NOT_FOUND,
            content={
                "status": ResponseStatus.ERROR,
                "message": message,
                "data": None,
            }
        )

    @staticmethod
    def error(message: str = Messages.INTERNAL_SERVER_ERROR, status_code: int = StatusCodes.HTTP_500_INTERNAL_SERVER_ERROR) -> JSONResponse:
        return JSONResponse(
            status_code=status_code,
            content={
                "status": ResponseStatus.ERROR,
                "message": message,
                "data": None,
            }
        )