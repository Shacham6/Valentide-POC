"""
    Description:
        `attrs` is doing everything.
        `valentide` ONLY generates the schema,
        labeled in the `VALENTIDE_SCHEMA` class variable.
"""
from collections import OrderedDict

from valentide import valentide, attrib


@valentide
class Person:
    name = attrib(type=str)
    age = attrib(type=int)


def test_schema_is_generated():
    assert hasattr(Person, 'VALENTIDE_SCHEMA')
    schema = Person.VALENTIDE_SCHEMA
    assert isinstance(schema, OrderedDict)
    assert schema['name'] == str
    assert schema['age'] == int
