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
creation.  It is also commonly overridden in custom meta classes in order to customize class creation.

__new__() has potential to create `magic` effects, which is why metaclasses are often considered more power than
99% of use cases that are ever necessary.
"""

from __future__ import annotations


class NormalNewReturn:

    def __new__(cls, x: int, y: int) -> NormalNewReturn:
        cls_instance = super().__new__(cls)
        cls_instance.x, cls_instance.y = x, y
        return cls_instance

    def __init__(self, x: int, y: int) -> None:
        """
        >>> NormalNewReturn(100, 200) #doctest: +ELLIPSIS
        Dunder __new__ returned an instance of `NormalNewReturn` so init was called
        ...
        """
        self.x = x
        self.y = y
        print("Dunder __new__ returned an instance of `NormalNewReturn` so init was called")


# -----


class A:

    def __new__(cls) -> A:
        return super().__new__(B)

    def __init__(self) -> None:
        """
        >>> A() #doctest: +ELLIPSIS
        Dunder init still gets called here..
        ...
        """
        print("Dunder init still gets called here..")

class B(A):
    ...


# -----


class NoInitHandoff:
    def __new__(cls) -> bool:
        print("Running __new__")
        return True

    def __init__(self) -> None:
        """
        >>> NoInitHandoff()
        Running __new__
        True
        """
        print("Not called")


# -----


"""
A practical example;  Lets say we are framework developers.  We are building out a common `BasePage`
for the `Page Object Model` in a selenium based test automation framework.  In order to prevent the 
users from passing a driver explicitly into each instantiation of the page, when creating a new instance
of the page, the __new__ functionality will implicitly inject a driver into the page, this is abstracted
away from the user and hidden deep in the framework.
"""


class Driver:
    def __init__(self) -> None:
        # Create some sort of delegate web driver
        ...

    def open_page(self, url: str) -> Driver:
        print("Opened:", url)
        return self


class BasePage:
    def __new__(cls) -> BasePage:
        instance = super().__new__(cls)
        instance.driver = Driver()
        return instance

class LoginPage(BasePage):
    """
    >>> LoginPage().load_login_page() #doctest: +ELLIPSIS
    I have a driver attr but never provided one
    Opened: https://mysite.com/app/login.php
    ...
    """
    def __init__(self) -> None:
        print("I have a driver attr but never provided one")

    def load_login_page(self) -> LoginPage:
        self.driver.open_page("https://mysite.com/app/login.php")
        return self


if __name__ == "__main__":
    import doctest
    doctest.testmod()