"""
Special method new (__new__) is called to create a new instance of cls.  __new__ is implicitly a `static_method`
special-cased so the user need not care declare it as such) that takes the class of which an instance was
requested as its first argument.  The remaining arguments are those passed to the object constructor expression
(the call to the class).  The return value of __new__() should be the new object instance, more often than not
an instance of cls.

Often mistaken for __init__(), __new__() is the real constructor of python objects, forwarding on the created
instance to __init__() when the type of instance created was that of the class only (more on that in the special
method init module).

Typical implementations create a new instance of the class by invoking the superclass's __new__() method using
super().__new__(cls[, ...]) with appropriate arguments and then modifyin the newly-created instance as necessary
before returning it.

if __new__() is invoked during object construction and it returns an instance or subclass of `cls`, then the
new instances `__init__()` method will be invoked like `__init__(self[, ...]), where self is the new instance
and the remaining arguments are the same as were passed to the object constructor.

if __new__() does not return an instance of `cls`, then the new instance's __init__() method will not be invoked.

__new__() is intended mainly to allow subclasses of immutable types (like int, str, or tuple) to customize instance
creation.  It is also commonly overriden in custom metaclasses in order to customize class creation.
"""

from __future__ import annotations
import typing

class New:

    def __new__(cls, name: str, bases: typing.Tuple[type, ...], attrs: typing.Dict[str, typing.Any]) -> New:
        return cls(name, bases, attrs)


if __name__ == "__main__":
    ...