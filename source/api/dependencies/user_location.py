from fastapi import Request
import requests


def get_location_from_ip(request: Request) -> dict:
    client_ip = request.client.host
    resp = requests.get(f"http://ip-api.com/json/{client_ip}")
    data = resp.json()
    return {"lat": data.get("lat"), "lon": data.get("lon")}