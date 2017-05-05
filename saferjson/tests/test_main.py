import unittest
import sys
from cStringIO import StringIO
from genty import genty, genty_dataset
from saferjson import main, dump_compact, dump_pretty


@genty
class main_tests (unittest.TestCase):

    _pretty_array = '[\n  "a",\n  "b",\n  42\n]'

    @genty_dataset(
        basic_number=([], '42', '42'),
        implicitly_pretty_array=([], '["a","b",42]', _pretty_array),
        explicitly_pretty_array=(['--pretty'], '["a","b",42]', _pretty_array),
        compact_array=(['--compact'], '["a","b",42]', '["a","b",42]'),
    )
    def test_basic(self, args, input, expectedoutput):
        with StdioPatcher(input) as sp:
            main.main(args)
            actualoutput = sp.stdout.getvalue()

        self.assertEqual(actualoutput, expectedoutput)


@genty
class parse_args_tests (unittest.TestCase):
    @genty_dataset(
        noargs=([], dump_pretty),
        explicit_pretty=(['--pretty'], dump_pretty),
        explicit_p=(['-p'], dump_pretty),
        explicit_compact=(['--compact'], dump_compact),
        explicit_c=(['-c'], dump_compact),
    )
    def test_format(self, args, expectedformat):
        opts = main.parse_args(args)
        self.assertIs(opts.FORMAT, expectedformat)

    def test_format_conflict(self):
        with StdioPatcher():
            self.assertRaises(
                SystemExit,
                main.parse_args,
                ['--pretty', '--compact'],
            )


class StdioPatcher (object):
    def __init__(self, input=''):
        self.input = input

    def __enter__(self):
        self.realstdin = sys.stdin
        self.realstdout = sys.stdout
        self.realstderr = sys.stderr

        sys.stdin = self.stdin = StringIO(self.input)
        sys.stdout = self.stdout = StringIO()
        sys.stderr = self.stderr = StringIO()

        return self

    def __exit__(self, et, ev, tb):
        sys.stdin = self.realstdin
        sys.stdout = self.realstdout
        sys.stderr = self.realstderr
