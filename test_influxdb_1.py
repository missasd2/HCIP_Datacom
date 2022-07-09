import pytest

def test_upper():
    assert "foo".upper() == "FOO1"


class TestClass:
    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        with pytest.raises(TypeError):
            x + []

