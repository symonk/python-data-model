"""
Special method `__setattr__()` is called when attribute assignment is requested.  This is called instead of the normal
assignment (assigning the value directly in `self.__dict__`).  `x.__setattr__(self, name, value)` is called with a name
and a value, where name is equivalent to the attribute name and value is the new value that should be assigned.

If `__setattr__()` wants to assign to an instance attribute, the base method should be invoked via the `super()` syntax.

Under some scenarios, surrounding sensitive attributes, access attributes on certain objects using `__setattr__()` creates
an event in the `audit events`
"""


class SettingAttrs:
  """
  >>> s = SettingAttrs(100, 200, 300)
  In setattr with a 100
  In setattr with b 200
  In setattr with c 300
  
  >>> s.z = 1337
  In setattr with z 1337
  
  >>> setattr(s, "x", 800)
  In setattr with x 800
  
  >>> s.__dict__['foo'] = 1280 # setattr is not called.
  
  """
  
  def __init__(self, a, b, c) -> None:
    self.a = a
    self.b = b
    self.c = c
    
  def __setattr__(self, name, value) -> None:
    print("In setattr with", name, value)
    super().__setattr(name, value)
    
    
if __name__ == "__main__":
  import doctest
  doctest.testmod()
