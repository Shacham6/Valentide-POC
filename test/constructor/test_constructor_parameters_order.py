"""
    Description:
        The order of the defined attributes in the class definition
        is the order of parameters in the constructor.
"""
from valentide import valentide, attrib


def test_order_1():
    @valentide
    class Foo:
        a = attrib()
        b = attrib()

    instance = Foo(1, 2)
    assert 1 == instance.a
    assert 2 == instance.b


def test_order_2():
    @valentide
    class Foo:
        b = attrib()
        a = attrib()

    instance = Foo(1, 2)
    assert 1 == instance.b
    assert 2 == instance.a
