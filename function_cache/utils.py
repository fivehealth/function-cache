__all__ = ['get_cache_key']

from hashlib import sha256
import json


def get_cache_key(args, kwargs, keys_args=[], keys_kwargs=[]):
    return sha256(json.dumps([args[i] for i in keys_args] + [kwargs.get(kw) for kw in keys_kwargs], ensure_ascii=True).encode('ascii')).hexdigest()
