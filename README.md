# Django Function Cache

[![PyPI version](https://img.shields.io/pypi/v/function-cache.svg)](https://pypi.python.org/pypi/function-cache/)
[![PyPI django version](https://img.shields.io/pypi/djversions/function-cache)](https://pypi.python.org/pypi/function-cache/)
[![PyPI license](https://img.shields.io/pypi/l/function-cache.svg)](https://pypi.python.org/pypi/function-cache/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/function-cache.svg)](https://pypi.python.org/pypi/function-cache/)
[![PyPI status](https://img.shields.io/pypi/status/function-cache.svg)](https://pypi.python.org/pypi/function-cache/)
[![PyPI download total](https://img.shields.io/pypi/dm/function-cache.svg)](https://pypi.python.org/pypi/function-cache/)

Cache the results of a function on S3 (and more!).
The `function_cache` decorator enables flexibility in how cache key is generated.

## Example

In your `settings.py`, you can set up the `FUNCTION_CACHE_BACKENDS` (defaults to [`S3FunctionCacheBackend`](function_cache/backends.py)):
```python
# Django Function Cache
# ---------------------
FUNCTION_CACHE_BACKENDS = {
    'default': {
        'BACKEND': 'function_cache.backends.S3FunctionCacheBackend',
        'OPTIONS': {},
    }
}
```

In your code, you can simply use the [`function_cache` decorator](function_cache/decorators.py)

```python
from django.contrib.staticfiles.storage import staticfiles_storage
from function_cache.decorators import function_cache


@function_cache(name='default', keys=('args[0]', 'args[1]', 'k'), storage=staticfiles_storage)
def create_dict(a, b, k=None, _cache_key=None):
    print(f'The cache key is <{_cache_key}>.')
    return dict(a=a, b=b, k=k)
#end def


def run():
    x = create_dict('variable a', 'b', k={'keyword argument': 42})
#end def
```
