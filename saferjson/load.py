import json
from decimal import Decimal


def load(f):
    return json.load(
        f,
        parse_float=Decimal,
        parse_int=Decimal,
        object_pairs_hook=_decode_obj_pairs,
    )


def loads(s):
    return json.loads(
        s,
        parse_float=Decimal,
        parse_int=Decimal,
        object_pairs_hook=_decode_obj_pairs,
    )


# Private:
def _decode_obj_pairs(items):
    d = {}
    for (k, value) in items:
        if k in d:
            raise ValueError('Duplicate key "{}".'.format(k))
        else:
            d[k] = value
    return d
