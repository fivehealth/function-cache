# Django Function Cache

Cache the results of a function on S3 (and more!).
The `function_cache` decorator enables flexibility in how cache key is generated.

## Example

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
