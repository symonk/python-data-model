"""
Special method `__getattr__(self, name)` is invoked automatically when default attribute access has failed.  Default
attribute access can fail in two ways:

    - `__getattribute__(self, name)` because `name` is not an instance attribute, or an attribute in the class tree
    of `self`, e.g its parent class etc.  This subsequently raises an `AttributeError`.

    - `__get__()` (part of the descriptor protocol) of a named property itself raises an `AttributeError`.

dunder `__getattr__()` itself should return the computed attribute value, or itself raise an `AttributeError`.

A common example of `__getattr__()` is used in the delegation pattern, where a class wrapping another class
wants to dispatch attribute access to its `self.delegate`.

In the event that either `__getattribute__` or `__get__` find an attribute by the name, dunder `__getattr__` is
never invoked, this is a notable difference from the `__setattr__` equivalent for setting attribute values.  This
is an intentional difference for efficiency reasons and also because otherwise `__getattr__` would have no way to
access other attributes of the instance.

In the case for instance variables, it is possible to fake total control by not inserting any attributes into
the instance dictionary `x.__dict__` but instead store them in another object altogether, you can read more
about this in the `dunder_getattribute.py` file in this files parent directory.
"""
import typing


class GetAttributeExample:
    """
    >>> GetAttributeExample(100).x
    100
    >>> GetAttributeExample(100).y
    Traceback (most recent call last):
    AttributeError: Unable to find: y in this instance
    """
    def __init__(self, x: int) -> None:
        self.x = x

    def __getattr__(self, name) -> typing.Any:
        # Don't do this in reality...
        raise AttributeError(f"Unable to find: {name} in this instance")


if __name__ == "__main__":
    import doctest
    doctest.testmod()