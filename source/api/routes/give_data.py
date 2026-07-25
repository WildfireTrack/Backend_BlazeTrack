from fastapi import APIRouter

from source.api.dependencies import fetch_global_widfire_data

router = APIRouter(tags=["GIVE DATA"])


@router.get("/")
def give_data():
    payload = fetch_global_widfire_data()
    return {"data": payload}