import unittest
from cStringIO import StringIO
from decimal import Decimal
from genty import genty, genty_dataset
from saferjson import load, loads


def load_wrapper(s):
    f = StringIO(s)
    return load(f)


@genty
class loads_tests (unittest.TestCase):
    @genty_dataset(
        from_int=('1',),
        from_float=('1.0',),
    )
    def test_decimal_parsing(self, input):
        expected = Decimal(input)
        for f in [loads, load_wrapper]:
            actual = f(input)
            self.assertIsInstance(actual, Decimal)
            self.assertEqual(expected, actual)

    @genty_dataset(
        load=(load_wrapper,),
        loads=(loads,),
    )
    def test_duplicate_keys_fail(self, f):
        self.assertRaisesRegexp(
            ValueError, r'Duplicate key "foo".',
            f, '{"foo": 42, "foo": 42}',
        )
