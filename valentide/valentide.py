from collections import OrderedDict

from attr import attrs, fields_dict


def valentide(cls):
    attrs_wrapper_cls = attrs(cls)
    attrs_wrapper_cls.VALENTIDE_SCHEMA = __generate_schema(fields_dict(attrs_wrapper_cls))
    return attrs_wrapper_cls


def __generate_schema(attrs_dict):
    valentide_schema = OrderedDict()
    for attr_name, attr_properties in attrs_dict.items():
        valentide_schema[attr_name] = attr_properties.type
    return valentide_schema
