from neomodel import (StructuredNode, StringProperty, IntegerProperty,
    UniqueIdProperty)


class Rule(StructuredNode):
    uid = UniqueIdProperty()
    name = StringProperty(unique_index=True, required=True)
    value = IntegerProperty(required=True)
    code = StringProperty(required=True)