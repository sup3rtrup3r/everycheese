import pytest
# from ..models import Cheese
from . factories import CheeseFactory

# Connects our tests with our databases
pytestmark = pytest.mark.django_db


def test____str__():
    # we replace this conde with our CheeseFactory
    # cheese = Cheese.objects.create(
    #     name="trapist",
    #     description="polutrvrdi kravlji sir, odlican uz suhomenatu platu",
    #     firmness=Cheese.Firmness.SEMI_HARD,
    # )
    cheese = CheeseFactory(name="Trapist")
    assert cheese.__str__() == cheese.name
    assert str(cheese) == cheese.name


def test__str__():
    cheese = CheeseFactory()
    assert cheese.__str__() == cheese.name
    assert str(cheese) == cheese.name


def test_cheese_get_absolute_url():
    cheese = CheeseFactory()
    url = cheese.get_absolute_url()
    assert url == f'/cheeses/{cheese.slug}/'
