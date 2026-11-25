from fastapi import APIRouter, HTTPException
from src.features.quiz.quiz_models import GetMenuItemsResponse, GetMenuItemResponse
from src.features.quiz import quiz_service

menu_item_router = APIRouter(
    prefix="/api/menu/items",
)


@menu_item_router.get("", response_model=GetMenuItemsResponse)
def get_menu_items():
    menu_items = quiz_service.get_menu_items()

    return {
        "menu_items": menu_items
    }

@menu_item_router.get("/{menu_items_id}", response_model=GetMenuItemResponse)
def get_menu_item_endpoint(menu_items_id: int):
    menu_item = quiz_service.get_menu_item(menu_items_id)

    if not menu_item:
        raise HTTPException(status_code=404)

    return {
        "menu_item": menu_item
    }


