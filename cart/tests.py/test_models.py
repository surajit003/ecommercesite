import pytest
from mixer.backend.django import mixer

pytestmark = pytest.mark.django_db


class TestCartModel:
    def test_cartitem(self):
        obj = mixer.blend("cart.CartItem")
        assert obj.pk == 1, "Should create a CartItem instance"
        assert str(obj) == "{} {}".format(obj.cart_id, obj.product.name)

    def test_cartitem_total(self):
        obj = mixer.blend("cart.CartItem")
        result = obj.quantity * obj.product.price
        assert obj.total() == result, "Product total for a CartItem"

    def test_product_name(self):
        obj = mixer.blend("cart.CartItem")
        assert obj.name() == obj.product.name, "Product name for a CartItem"

    def test_product_price(self):
        obj = mixer.blend("cart.CartItem")
        assert obj.price() == obj.product.price, "Product price for a CartItem"

    def test_get_absolute_url(self):
        obj = mixer.blend("cart.CartItem")
        assert obj.get_absolute_url() == obj.product.get_absolute_url(), "Product link"

    def test_augment_quantity(self):
        obj = mixer.blend("cart.CartItem", quantity=3)
        obj.augment_quantity(4)
        assert obj.quantity == 7, "augment initial product quantity in cart item"
