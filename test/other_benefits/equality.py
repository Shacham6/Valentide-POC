from valentide import valentide, attrib


@valentide
class Person:
    name = attrib(type=str)
    age = attrib(type=int)


def test_to_equal_persons_are_equal_much_wow():
    name = 'Bruce Campbell'
    age = 60

    assert Person(name, age) == Person(name, age)
    assert Person(name, age) is not Person(name, age)
