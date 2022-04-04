import uvicorn
from fastapi import FastAPI
from fastapi.openapi.docs import get_swagger_ui_html
import os

from core.config import SERVER_HOST, SERVER_PORT
from endpoints import items, s3, liveness_probe

app = FastAPI(openapi_url="/api/v1/openapi.json", swagger_ui_oauth2_redirect_url="/api/v1/docs/oauth2-redirect")


app.include_router(s3.router)
app.include_router(liveness_probe.router)
app.include_router(items.router)


@app.get("/api/v1/docs", include_in_schema=False)
async def get_documentation():
    return get_swagger_ui_html(openapi_url="openapi.json", title="Swagger")


if __name__ == "__main__":
    # os.system('alembic upgrade head')
    uvicorn.run("main:app", port=SERVER_PORT, host=SERVER_HOST, reload=True)
