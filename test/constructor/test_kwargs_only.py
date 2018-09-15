"""
    Description:
        `attrs` allows us to modify the way we receive parameters in the
        constructor.
        In this example, we define a parameter that can only be received
        in kwargs.
"""
import pytest

from valentide import valentide, attrib


@valentide
class Foo:
    a = attrib()
    b = attrib(kw_only=True)


def test_all_kwargs():
    instance = Foo(a=1, b=2)
    assert 1 == instance.a
    assert 2 == instance.b


def test_fails_when_b_as_positional_arg():
    with pytest.raises(TypeError):
        Foo(1, 2)
