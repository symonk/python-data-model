"""
Special method `__get_attribute__` is called unconditionally for attribute access for instances of the class.
If a class implements its own `__getattr__` it will never be called unless a few criteria are met:

 - `__getattribute__` explicitly calls it.
 - `__getattribute__` raises an `AttributeError`.
 - `__get__` of a named property raises an `AttributeError`

`__getattribute__` should return the (computed) value of the attribute and to avoid the scenario of infinite
recursion, should defer to the `super()` implementation of `__getattribute__`.

Similarly to `__setattr__` under some sensitive scenarios, an `audit event` is logged.
"""


class SimpleGetAttribute:
    """
    >>> s = SimpleGetAttribute(10, 20, 30)
    >>> s.a
    in dunder getattribute, looking for: a
    10
    >>> s.x
    Traceback (most recent call last):
    AttributeError: 'SimpleGetAttribute' object has no attribute 'x'
    >>> s.kls_attr
    in dunder getattribute, looking for: kls_attr
    100
    >>> s.__dict__
    in dunder getattribute, looking for: __dict__
    {'a': 10, 'b': 20, 'c': 30}
    """
    kls_attr = 100

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __getattribute__(self, item: str):
        # Avoid infinite recursion by invoking the base classes getattribute explicitly
        print("in dunder getattribute, looking for:", item)
        return super().__getattribute__(item)


if __name__ == "__main__":
    import doctest
    doctest.testmod()