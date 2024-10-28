from fastapi import APIRouter

from app.api.routes import location_routes, clothes_routes, user_routes

api_router = APIRouter()
api_router.include_router(location_routes.router)
api_router.include_router(clothes_routes.router)
api_router.include_router(user_routes.router)