from valentide import valentide, attrib


@valentide
class Person:
    name = attrib(type=str)
    age = attrib(type=int)


def test_looking_good_as_string():
    bruce_campbell = Person(
        name='Bruce Campbell',
        age=60,
    )
    assert str(bruce_campbell) == 'Person(name=\'Bruce Campbell\', age=60)'
