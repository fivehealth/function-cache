__all__ = ['BaseFunctionCacheBackend', 'S3FunctionCacheBackend', 'get_cache_backend']
from functools import lru_cache
from hashlib import sha256
from itertools import chain
import json
import logging
import re

from django.conf import settings
from django.core.files.base import ContentFile
from django.utils.module_loading import import_string

ARGS_REGEX = re.compile(r'^args\[(\d+)\]$')

logger = logging.getLogger(__name__)


@lru_cache()
def get_cache_backend(name='default', keys=None, **kwargs):
    d = settings.FUNCTION_CACHE_BACKENDS[name]
    backend_class = import_string(d['BACKEND'])
    options = dict((k, v) for k, v in chain(d.get('OPTIONS', {}).items(), kwargs.items()))

    if keys is None:
        keys = options.pop('keys', None)

    return backend_class(keys=keys, **options)
#end def


class BaseFunctionCacheBackend():
    def __init__(self, keys=None, serializer=None, deserializer=None, **kwargs):
        args_keys, kwargs_keys = [], []

        if keys:
            for k in keys:
                m = ARGS_REGEX.match(k)
                if m:
                    args_keys.append(int(m.group(1)))
                else:
                    kwargs_keys.append(k)
                #end if
            #end for
        #end if

        self.args_keys = args_keys
        self.kwargs_keys = kwargs_keys

        self.serializer = serializer or self.default_serializer
        self.deserializer = deserializer or self.default_deserializer
    #end def

    def default_serializer(self, result):
        return json.dumps(result, ensure_ascii=True).encode('ascii')

    def default_deserializer(self, content):
        return json.loads(content)

    def compute_key(self, args, kwargs):
        if self.args_keys or self.kwargs_keys:
            L = [args[i] for i in self.args_keys] + [kwargs.get(kw) for kw in self.kwargs_keys]
        else:
            L = list(args) + list(kwargs.values())
        #end if

        return sha256(json.dumps(L, ensure_ascii=True).encode('ascii')).hexdigest()
    #end def

    def exists(self, cache_key):
        raise NotImplementedError()

    def get(self, cache_key):
        raise NotImplementedError()

    def put(self, cache_key, result):
        raise NotImplementedError()
#end class


class DummyFunctionCacheBackend():
    def exists(self, cache_key):
        return False

    def put(self, cache_key, result):
        return
#end class


class S3FunctionCacheBackend(BaseFunctionCacheBackend):
    def __init__(self, storage=None, **kwargs):
        super().__init__(**kwargs)

        self.storage = storage
        assert storage is not None
    #end def

    def exists(self, cache_key):
        hit = self.storage.exists(cache_key)
        return hit
    #end def

    def get(self, cache_key):
        content = self.storage.open(cache_key).read()
        logger.debug(f'S3FunctionCacheBackend read {len(content)} bytes for cache key <{cache_key}>.')
        return self.deserializer(content)
    #end def

    def put(self, cache_key, result):
        content = self.serializer(result)
        logger.debug(f'S3FunctionCacheBackend saved {len(content)} bytes for cache key <{cache_key}>.')
        self.storage.save(cache_key, ContentFile(content))
    #end def
#end class
