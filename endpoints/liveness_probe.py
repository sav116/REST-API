from fastapi import APIRouter, status
from endpoints.base import prefix

router = APIRouter(prefix=prefix)


@router.get("/healthz", status_code=status.HTTP_200_OK)
async def get_healthz():
    return {"status": "healthy"}


@router.get("/", status_code=status.HTTP_200_OK)
async def get_root():
    return {"status": "healthy"}
