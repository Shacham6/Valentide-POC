"""
    Description:
        An example to show the constructors generated
        by the attrs library.
"""
from valentide import valentide, attrib


@valentide
class Person:
    name = attrib(type=str)
    age = attrib(type=int)


def test_positional_args_in_generated_constructor():
    bruce_campbell = Person('Bruce Campbell', 60)
    assert 'Bruce Campbell' == bruce_campbell.name
    assert 60 == bruce_campbell.age


def test_named_args_in_generated_constructor():
    bruce_campbell = Person(name='Bruce Campbell', age=60)
    assert 'Bruce Campbell' == bruce_campbell.name
    assert 60 == bruce_campbell.age
