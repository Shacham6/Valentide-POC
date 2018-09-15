from valentide import valentide, attrib


@valentide
class Person:
    name = attrib(type=str)
    age = attrib(type=int)


@valentide
class AmericanPerson(Person):
    """
    An american person is a _special_ type of person
    """

    has_a_gun = attrib(type=bool)


def test_american_person_accepts_persons_parameters():
    bruce_campbell = AmericanPerson(name='Bruce Campbell', age=60, has_a_gun=True)

    assert isinstance(bruce_campbell, Person)

    assert bruce_campbell.name == 'Bruce Campbell'
    assert bruce_campbell.age == 60
    assert bruce_campbell.has_a_gun

    schema = AmericanPerson.VALENTIDE_SCHEMA
    assert schema['name'] == str
    assert schema['age'] == int
    assert schema['has_a_gun'] == bool
