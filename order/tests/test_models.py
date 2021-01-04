import pytest
from mixer.backend.django import mixer

pytestmark = pytest.mark.django_db


class TestOrderModel:
    def test_order(self):
        obj = mixer.blend("order.Order")
        assert obj.pk == 1, "Should create a Order instance"
        assert str(obj) == "{}".format(obj.user.username)
