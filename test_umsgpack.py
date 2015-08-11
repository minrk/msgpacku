from umsgpack import packb, unpackb

def roundtrip(obj):
    """roundtrip an object"""
    return unpackb(packb(obj))

def test_roundtrip_bytes():
    a = b'buffer'
    b = roundtrip(a)
    assert a == b
    assert type(a) is type(b)

def test_roundtrip_text():
    a = u'text'
    b = roundtrip(a)
    assert a == b
    assert type(a) is type(b)
