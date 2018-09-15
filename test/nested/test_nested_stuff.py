from valentide import valentide, attrib


@valentide
class Name:
    first = attrib(type=str)
    last = attrib(type=str)


@valentide
class Person:
    name = attrib(type=Name)
    age = attrib(type=int)


def test_positional_init():
    bruce_campbell = Person(Name('Bruce', 'Campbell'), 60)
    assert bruce_campbell.name.first == 'Bruce'
    assert bruce_campbell.name.last == 'Campbell'
    assert bruce_campbell.age == 60

    assert bruce_campbell == Person(Name('Bruce', 'Campbell'), 60)

    assert Person.VALENTIDE_SCHEMA['name'] == Name
    assert Person.VALENTIDE_SCHEMA['age'] == int
