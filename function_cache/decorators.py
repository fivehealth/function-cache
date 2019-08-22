__all__ = ['function_cache']
from functools import wraps
from inspect import signature
import logging

from .backends import get_cache_backend

logger = logging.getLogger(__name__)


def function_cache(name='default', keys=None, **kwargs):
    cache_backend = get_cache_backend(name, keys=keys, **kwargs)

    def decorator(decorated_func):
        sig = signature(decorated_func)
        pass_cache_key = '_cache_key' in sig.parameters or any(param.kind == param.VAR_KEYWORD for param in sig.parameters.values())

        @wraps(decorated_func)
        def wrapper(*args, **kwargs):
            cache_key = cache_backend.compute_key(args, kwargs)

            cache_hit = cache_backend.exists(cache_key)
            logger.debug(f'Cache {"hit" if cache_hit else "miss"} for cache key <{cache_key}>.')
            if cache_hit:
                return cache_backend.get(cache_key)

            if pass_cache_key:
                result = decorated_func(*args, **kwargs, _cache_key=cache_key)
            else:
                result = decorated_func(*args, **kwargs)
            #end if

            cache_backend.put(cache_key, result)

            return result
        #end def

        return wrapper
    #end def

    return decorator
#end def