import pytest
from ..models import Cheese

# Connects our tests with our databases
pytestmark = pytest.mark.django_db


def test____str__():
    cheese = Cheese.objects.create(
        name="trapist",
        description="polutrvrdi kravlji sir, odlican uz suhomenatu platu",
        firmness=Cheese.Firmness.SEMI_HARD,
    )
    assert cheese.__str__() == "trapist"
    assert str(cheese) == "trapist"
