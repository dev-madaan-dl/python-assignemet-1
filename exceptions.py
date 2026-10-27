from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
import httpx


async def not_found_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=404,
        content={"error": "Not Found", "detail": f"Path '{request.url.path}' does not exist"}
    )


async def validation_error_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content={"error": "Validation Error", "detail": exc.errors()}
    )


async def timeout_handler(_request: Request, _exc: httpx.TimeoutException):
    return JSONResponse(
        status_code=504,
        content={"error": "Gateway Timeout", "detail": "External service timed out"}
    )


async def connect_error_handler(_request: Request, _exc: httpx.ConnectError):
    return JSONResponse(
        status_code=502,
        content={"error": "Bad Gateway", "detail": "Could not reach external service"}
    )


async def internal_error_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"error": "Internal Server Error", "detail": "Something went wrong on our end"}
    )


def register_exception_handlers(app: FastAPI):
    app.add_exception_handler(404, not_found_handler)
    app.add_exception_handler(RequestValidationError, validation_error_handler)
    app.add_exception_handler(httpx.TimeoutException, timeout_handler)
    app.add_exception_handler(httpx.ConnectError, connect_error_handler)
    app.add_exception_handler(Exception, internal_error_handler)
