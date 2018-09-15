from valentide import valentide, attrib


@valentide
class PersonName:
    first_name = attrib(type=str, kw_only=True)
    middle_name = attrib(type=str, default=None, kw_only=True)
    last_name = attrib(type=str, kw_only=True)


def test_not_providing_middle_name():
    name = PersonName(first_name='Bruce', last_name='Campbell')
    assert name.first_name == 'Bruce'
    assert name.middle_name is None
    assert name.last_name == 'Campbell'


def test_providing_middle_name():
    name = PersonName(first_name='Bruce', middle_name='Ash', last_name='Campbell')
    assert name.first_name == 'Bruce'
    assert name.middle_name == 'Ash'
    assert name.last_name == 'Campbell'
