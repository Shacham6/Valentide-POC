from valentide import valentide, attrib


@valentide
class Person:
    name = attrib(type=str)
    age = attrib(type=int)


@valentide
class Child(Person):
    parent = attrib(type=Person)


def test_same_as_the_just_inheritance_tests():
    bruce_campbell = Child(
        name='Bruce Campbell',
        age=60,
        parent=Person(
            name='Bruce Campbell\'s parent',
            age=61,
        ),
    )

    assert isinstance(bruce_campbell, Person)
    assert isinstance(bruce_campbell, Child)
    assert bruce_campbell.name == 'Bruce Campbell'
    assert bruce_campbell.age == 60
    assert bruce_campbell.parent == Person(
        name='Bruce Campbell\'s parent',
        age=61
    )
