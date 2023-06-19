from src.models.ingredient import Ingredient  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingredient = Ingredient("Tomato")
    assert ingredient.name == "Tomato"
    assert ingredient.restrictions == set()

    ingredient = Ingredient("Tomato")
    assert repr(ingredient) == "Ingredient('Tomato')"

    ingredient1 = Ingredient("Tomato")
    ingredient2 = Ingredient("Tomato")
    ingredient3 = Ingredient("Onion")

    assert ingredient1 == ingredient2
    assert ingredient1 != ingredient3

    ingredient1 = Ingredient("Tomato")
    ingredient2 = Ingredient("Tomato")
    ingredient3 = Ingredient("Onion")

    assert hash(ingredient1) == hash(ingredient2)
    assert hash(ingredient1) != hash(ingredient3)
