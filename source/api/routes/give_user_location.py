from fastapi import APIRouter, Request
from source.api.dependencies.user_location import get_location_from_ip

router = APIRouter(prefix='', tags=["USER LOCATION"])


@router.get('/location')
def get_location(request: Request) -> dict:
    data = get_location_from_ip(request)
    return {"lat": data["lat"], "lon": data["lon"]}