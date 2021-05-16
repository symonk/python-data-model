# python-data-object-model

-----

## 3.3 Special Method Names

A class can implement certain operations that are invoked by special syntax (such as arithmetic operations, subscripting 
and slicing) by defining methods with special names.  This is Pythons approach to operator overloading, allowing classes
to define their own behaviour with respect to language operators.  For instance, if a class defines a method named 
`__getitem__(obj, item)` and obj is an instance of this class, then `obj[item]` is roughly equivalent to 
`type(obj).__getitem__(obj, item)`.  Except where mentioned, attempts to execute an operation raise an exception
when no appropriate method is defined (typically `AttributeError` or `TypeError`).

Setting special methods to `None` explicitly indicates that the corresponding operation is not available.  For example,
if a class sets `__iter__(self)` to `None`, the class is not iterable, so calling `iter(x)` where x is an instance of
such class will raise a `TypeError` without failing back to `__getitem__()`.

When implementing a class that emulates any built-in type, it is important that the emulation only be implemented to
the degree that it makes sense for the object being modelled.  For example, some sequences may work well with retrieve 
of individual elements, but extracting a slice from them may not make sense.  One example of this is the `NodeList`
interface in the `W3Cs Document Object Model`.