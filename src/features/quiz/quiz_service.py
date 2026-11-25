import pandas as pd
from src.features.quiz.quiz_models import MenuItem

MENU_ITEMS_FILE_PATH = "menu.csv"

def load_menu_items()-> list[MenuItem]:
    menu_items = []
    df =pd.read_csv(MENU_ITEMS_FILE_PATH, sep=';')

    for row in df.itertuples(index=False):
        menu_item = MenuItem(id=row.id,
                             category=row.category,
                             name=row.name,
                             description=row.description,
                             ingredients=row.ingredients,
                             price=row.price
                            )
        menu_items.append(menu_item)
    return menu_items

MENU_ITEMS = load_menu_items()

def get_menu_items() -> list[MenuItem]:
    return MENU_ITEMS

def get_menu_item(id : int) -> MenuItem |None:
   for menu_item in MENU_ITEMS:
       if menu_item.id == id:
           return menu_item

   return None




