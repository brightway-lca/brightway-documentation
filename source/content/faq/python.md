# Python

## How can I find out what kind of Python object I am dealing with?

You can use the `type` function to find out what kind of Python object you are dealing with:

```python
type(my_object)
```

This may not always be helpful. This is because many Brightway objects are instances of classes that inherit from other classes. To find out which classes an object inherits from, you can use the `inspect` module:

```python
import inspect
print(inspect.getmro(type(my_object)))
```

For example, if we want to find out what kind of object a random activity from a database is, we can do the following:

```python
import bw2data as bd
import inspect
my_database = bd.Database('<database_name>')
print(inspect.getmro(type(my_database.random())))
```

This will tell us that, a few levels of down, the object is an instance of `Mapping`, [which is most frequently used in Python to represent a dictionary](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict):

```
(
    <class 'bw2data.backends.proxies.Activity'>,
    <class 'bw2data.proxies.ActivityProxyBase'>,
    <class 'bw2data.proxies.ProxyBase'>,
    <class 'collections.abc.MutableMapping'>,
    <class 'collections.abc.Mapping'>,
    <class 'collections.abc.Collection'>,
    <class 'collections.abc.Sized'>,
    <class 'collections.abc.Iterable'>,
    <class 'collections.abc.Container'>,
    <class 'object'>
)
```