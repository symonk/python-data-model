"""
Special method `__delattr__` is similar to `__setattr__` but is used for attribute deletion
rather than assignment.  Objects should only implement `__delattr__` if it is somewhat meaningful
to the object.

Like `__setattr__` in some sensitive scenarios it can write and audit event.

"""

class DelAttr:
    """
    >>> d = DelAttr()
    >>> delattr(d, "b")
    in del attr!
    >>> d.__dict__
    {'a': 100}
    """
    def __init__(self) -> None:
        self.a = 100
        self.b = "test"

    def __delattr__(self, item):
        print("in del attr!")
        super().__delattr__(item)


if __name__ == "__main__":
    import doctest
    doctest.testmod()