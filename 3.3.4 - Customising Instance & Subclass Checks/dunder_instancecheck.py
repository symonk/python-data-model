"""
Special method `__instancecheck__` is used to override the default behaviour of the `isinstance()`
for user defined classes.  One common example of `__instancecheck__` is in the abc package ABCMeta 
metaclass, which permits virtual subclasses (classes which do not explicitly inherit from a particular
parent, but instead are registered after the factor through the @register decorator.

`__instancecheck__(instance)` should return a boolean (True) if the instance should be considered
either a direct, or indirect instance of class.  If defined called as part of isinstance(instance, clazz)

Important note: `__instancecheck__` is not looked up on the instance itself, but rather the metaclass
of a class, it cannot be defined as explicit class method in the class.
"""
