from src.models.dish import Dish  # noqa: F401, E261, E501
import pytest


# Req 2
def test_dish():
    dish = Dish("Carbonara", 14.99)
    assert dish.name == "Carbonara"
    assert dish.price == 14.99

    dish1 = Dish("Carbonara", 14.99)
    dish2 = Dish("Carbonara", 14.99)
    assert hash(dish1) == hash(dish2)

    dish1 = Dish("Carbonara", 14.99)
    dish2 = Dish("Pizza", 44.99)
    assert hash(dish1) != hash(dish2)

    dish1 = Dish("Carbonara", 14.99)
    dish2 = Dish("Carbonara", 14.99)
    dish3 = Dish("Pizza", 44.99)
    assert dish1 == dish2
    assert dish1 != dish3

    dish = Dish("Carbonara", 14.99)
    assert repr(dish) == "Dish('Carbonara', R$14.99)"

    with pytest.raises(TypeError):
        Dish("Carbonara", "14.99")

    with pytest.raises(ValueError):
        Dish("Carbonara", -14.99)

    dish = Dish("Carbonara", 14.99)
    assert dish.get_restrictions() == set()

    dish = Dish("Carbonara", 14.99)
    dish.add_ingredient_dependency("pasta", 200)
    dish.add_ingredient_dependency("bacon", 300)
    dish.add_ingredient_dependency("cheese", 100)

    assert dish.get_ingredients() == {'pasta', 'bacon', 'cheese'}
