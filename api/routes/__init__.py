from fastapi import APIRouter

from .pessoas_route import router as pessoas_router

main_router = APIRouter()

main_router.include_router(pessoas_router, prefix="/pessoas", tags=["pessoas"])
