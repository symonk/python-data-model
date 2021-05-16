"""
Special method `__del__()` is called when the instance of an object is about to be destroyed.  This is also known
as a `finalizer` and occasionally incorrectly considered a `destructor`.  Similar to `__init__()` in an inheritance
based setup, if a base class implements a `__del__()` then subsequent child classes should also implement their
`__del__()` which calls the base classes via `super()` in order to guarantee deletion of the base parts of the
instance.

It is possible but ill-advised for the `__del__()` implementation of an instance to postpone the destruction of
itself by having `__del__()` create a new reference to it.  This is known as `Object Resurrection`.  It is an
implementation detail whether or not the python interpreter will attempt to finalize resurrected objects by invoking
their `__del__()` method twice, `CPython` currently will only attempt to call `__del__()` one time regardless.

There is NO guarantee that `__del__()` on objects that still exist when the interpreter is exiting will be called,

The builtin `del` is often confused with mapping directly to an objects `__del__()` invocation, for example it is
often misunderstood that `del x` is not the equivalent of `x.__del__()`.  The former (`del x`) simply decrements
the reference count of `x` by 1.  The latter `x.__del__()` is invoked when the reference count reaches 0.

It is possible for the reference count of an object in python to be prevented from reaching 0 and subsequently firing
`__del__()` on its instance.  As far as the reference count garbage collection goes this instance is in limbo,
however this is why python has a two pronged approach to garbage collection, the `cyclic garbage collector` will
be able to collect such instances later and free them.

One of the most common examples where the `cyclic garbage collector` is required is when an exception has been caught
in a local variable, the frames locals then reference the exception which in turn references its own traceback which
subsequently references all the locals of all frames in the traceback.

Exceptions raised in a `__del__()` implementation are ignored by python, in exchange a warning is written to
sys.stderr

TBC...
"""



if __name__ == "__main__":
    ...