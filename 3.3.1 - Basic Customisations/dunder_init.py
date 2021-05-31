"""
Special method `__init__()` is called after the object has been created.  This is denoted by the
`self` argument (vs the `cls` of `__new__()`).  When special method `__new__()` returns either an instance
or subclass of the class in question, its special method `__init__()` is invoked.  This is called before
the instance is returned to the caller.  Additional arguments passed to `__init__(self, *args, **kwargs)` are
those passed to the class constructor.  If the base class has a special `__init__()` declared, subclasses should
explicitly invoke this to guarantee initialization of the base class part of the instance.

`__init__()` must not return anything other than `None` or a `TypeError` is raised.
"""


class BasicInit:
    def __init__(self, a: int = 1, b: str = "") -> None:
        self.a = a
        self.b = b

class BasicInitSub(BasicInit):
    def __init__(self, a: int = 1, b: str = "") -> None:
        super().__init__(a, b)

class RaisesTypeError:
    def __init__(self) -> None:
        return True  # TypeError


if __name__ == "__main__":
    BasicInit(1, "two")
    BasicInitSub(1, "two")
    RaisesTypeError()