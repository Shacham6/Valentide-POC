from collections import OrderedDict
from valentide import valentide, attrib


def test_order_1():
    @valentide
    class Foo:
        a = attrib(type=str)
        b = attrib(type=int)

    manual_schema = OrderedDict()
    manual_schema['a'] = str
    manual_schema['b'] = int

    assert Foo.VALENTIDE_SCHEMA == manual_schema


def test_order_2():
    @valentide
    class Foo:
        b = attrib(type=int)
        a = attrib(type=str)

    manual_schema = OrderedDict()
    manual_schema['b'] = int
    manual_schema['a'] = str

    assert Foo.VALENTIDE_SCHEMA == manual_schema
