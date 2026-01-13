# standardize the response
from fastapi.responses import JSONResponse


def standardize_response(data: any, custom_message: str = None):
    return JSONResponse(
        content={"data": data, "message": custom_message},
        status_code=200,
    )
