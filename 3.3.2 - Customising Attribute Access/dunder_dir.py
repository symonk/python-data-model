"""
Special method `__dir__()` is used to list either attributes in the local scope (when the optional
object parameter is omitted, or a list of valid attributes if object is provided).  Custom implementations
of `__dir__()` are called by the builtin `dir()` function and as per the data model should return a
sequence of items (attributes).

`__dir__` is often used in conjunction with either `__getattribute__` or `__getattr__` to customise the
way the objects attributes are reported.

if `__dir__` is omitted altogether on an object, python will attempt to derive something reasonable from
the objects `__dict__` if defined as well as its type object, however due to the dynamic nature of the
language the list is not complete and especially in cases where the obj has implemented `__getattr__`.

`__dir__` should ideally return a sorted list, as if an unsorted non-list sequence is returned python
itself will both convert to a list and sort the list.

`dir()` itself is often useful from the python interpreter/prompt and is not required to be explicitly
correct, it attempts to supply a convenient set of names rather than a completely accurate set.
"""

def module_level_attributes_via_dir():
    """
        import struct
        >>> dir()  #doctest: +ELLIPSIS
        [... '__annotations__', '__builtins__', ... 'module_level_attributes_via_dir']
    """
    ...


class C:
    def __init__(self, a, b):
        self.a = a
        self.b = b


def class_level_attribute_via_dir():

    """
    >>> c = C(100, 200)
    >>> dir(c) #doctest:  +ELLIPSIS
    ['__class__', ... 'a', 'b']
    """
    ...

class Custom:
    """
    >>> c = Custom()
    >>> dir(c)
    ['a', 'b', 'c', 'd', 'y', 'z']
    """
    def __init__(self):
        self.a = 10
        self.b = 20
        self.c = 30
        self.z = 40
        self.y = 50
        self.d = 60

    def __dir__(self):
        # return the keys in sorted order
        # even tho we make an unsorted tuple here, a list of sorted items is returned by dir(Custom())
        return tuple(self.__dict__)


if __name__ == "__main__":
    import doctest
    doctest.testmod()