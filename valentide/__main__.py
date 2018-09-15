from valentide import valentide, attrib


@valentide
class Person:
    name = attrib(type=str, kw_only=True)
    age = attrib(type=int, kw_only=True)


@valentide
class Child(Person):
    parent = attrib(type=Person, kw_only=True)


# Wow cool constructor
child = Child(
    name='Bruce Campbell',
    age=16,
    parent=Person(
        name='Bruce Campbell\'s parent',
        age=20
    ),
)
