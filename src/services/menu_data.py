import csv
from models.dish import Dish
from models.ingredient import Ingredient


# Req 3
class MenuData:
    def __init__(self, source_path: str):
        self.dishes = set()
        self._load_menu_data(source_path)

    def _load_menu_data(self, source_path: str):
        with open(source_path, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                dish_name = row["dish"]
                dish_price = float(row["price"])
                ingredient_name = row["ingredient"]
                recipe_amount = int(row["recipe_amount"])
                dish = self._get_dish(dish_name, dish_price)
                ingredient = Ingredient(ingredient_name)
                dish.add_ingredient_dependency(ingredient, recipe_amount)

    def _get_dish(self, dish_name: str, dish_price: float) -> Dish:
        for dish in self.dishes:
            if dish == Dish(dish_name, dish_price):
                return dish
        dish = Dish(dish_name, dish_price)
        self.dishes.add(dish)
        return dish
