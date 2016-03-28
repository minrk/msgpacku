# msgpacku - unicode-friendly msgpack wrapper

`msgpacku` is a unicode-friendly msgpack wrapper. This does only one thing to each of `packb` and `unpackb`:
change the defaults of msgpack-python to use the binary type by default,
and decode text as utf8 by default.

See [msgpack-python#99](https://github.com/msgpack/msgpack-python/issues/99) for context.

## Install

    pip intall msgpacku

## Usage

To use: replace calls to `msgpack.[un]packb` with `msgpacku.[un]packb`.
e.g.

```python
In [1]: import msgpack, msgpacku

In [2]: msgpack.unpackb(msgpack.packb(u'text'))
Out[2]: b'text'

In [3]: msgpacku.unpackb(msgpacku.packb(u'text'))
Out[3]: u'text'
```

