from fastapi import APIRouter

from source.api.routes.give_data import router as give_data_router

router = APIRouter()

router.include_router(give_data_router)