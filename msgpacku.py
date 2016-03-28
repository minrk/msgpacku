"""Wrap msgpack in more Python 3-friendly defaults for text

ensures binary and text types are kept separate

"""
import msgpack
from msgpack import *

__version__ = '0.1.0'

def packb(obj, **kwargs):
    """wrap msgpack.packb, setting use_bin_type=True by default"""
    kwargs.setdefault('use_bin_type', True)
    return msgpack.packb(obj, **kwargs)

def unpackb(buf, **kwargs):
    """wrap msgpack.unpackb, setting encoding='utf8' by default"""
    kwargs.setdefault('encoding', 'utf8')
    return msgpack.unpackb(buf, **kwargs)
