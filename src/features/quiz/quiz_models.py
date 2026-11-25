from pydantic import BaseModel

class MenuItem(BaseModel):
    id : int
    category : str
    name : str
    description : str
    ingredients : str
    price : float


class GetMenuItemsResponse(BaseModel):
    menu_items: list[MenuItem]

class GetMenuItemResponse(BaseModel):
    menu_item: MenuItem

