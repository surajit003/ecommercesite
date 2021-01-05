import pytest
from cart.tools import generate_cart_id

pytestmark = pytest.mark.django_db


class TestCartTool:
    def test_generate_cart_id(self):
        result = generate_cart_id()
        assert len(result) == 50
        result1 = generate_cart_id
        assert result1 != result, "should evaluate to false"
