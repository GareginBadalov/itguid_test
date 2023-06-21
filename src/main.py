import uvicorn
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from starlette.middleware.cors import CORSMiddleware

import config
from api.api_v1.api import api_router

app = FastAPI(
    title=config.project_name, openapi_url=f"{config.api_v1_path}/openapi.json"
)

app.include_router(
    api_router, prefix=config.api_v1_path
)

if config.backend_cors_origins:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=config.backend_cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title=config.project_name,
        version="0.1.0",
        description=f"{config.project_name} API",
        routes=app.routes,
    )
    openapi_schema['components']['securitySchemes'] = {
        'OAuth2PasswordBearer': {
            'type': 'apiKey',
            'in': 'header',
            'name': 'Authorization',
            'description': 'Enter: **"Bearer &lt;JWT&gt;"**, where JWT is the access token'
        }
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi

if __name__ == '__main__':
    uvicorn.run("main:app", host="localhost", log_level="info")
