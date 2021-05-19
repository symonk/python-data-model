"""

The `None` type in python has a single value, there exists a single object with that value.  The object with
the value None is accessible through the builtin `None` name.  It is used to signify the absense of a value
in various different situations.

It is implicitly returned from functions which do not specify a return value.

In a boolean context, it's value is `False`.

Note: In python `3.10` types.NoneType will be re-added back into the language
"""

def implicitly_none() -> None:
    ...


if __name__ == "__main__":
    print(implicitly_none())  # None
    print(type(implicitly_none()))  # <class 'NoneType'>
    print(bool(implicitly_none()))  # False
