"""
Special method `__init_subclass__` is invoked when the implementing class is subclassed.  It is important to note
that this is executed when the class is subclassed and not when the subclass is instantiated.  This permits writing
classes that at runtime can modify the class behaviour of it's subclasses.  This is similar to class decorators however
the former requires explicit decoration whereas `__init_subclass__` is implicitly applied to all subclasses.

When defined as a normal instance method; this is implicitly converter to a class method where the `cls` attribute
is the new class subclass (class not instance).

  ```
  classmethod object.__init_subclass__(cls)
  
  Default implementation of `__init_sublass__` in `object` is to do nothing and raise a `TypeError`
  
  class ObjectInitSubclass(foo='bar'):
    ...
  TypeError: ObjectInitSubclass.__init_subclass__() takes no keyword arguments
  ```
"""

class BespokeSubclasses:
  def __init_subclass__(cls, /, default_number, **kwargs):
    super().__init_subclass__(**kwargs)
    cls.default_number = default_number
    
class MySubClass(BespokeSubClasses, default_number=1337):
    # default_number class attr is 1337 for  
    ...
    
