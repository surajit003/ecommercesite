import pytest
from mixer.backend.django import mixer

pytestmark = pytest.mark.django_db


class TestCatalog:
    def test_category(self):
        obj = mixer.blend("catalog.Category")
        assert obj.pk == 1, "Should create a Category instance"
        assert str(obj) == "{}".format(obj.name)
