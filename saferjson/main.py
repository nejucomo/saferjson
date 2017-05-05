import sys
import argparse
from saferjson import load, dump_compact, dump_pretty


def main(args=sys.argv[1:]):
    """
    Canonicalize a json source from stdin to stdout.
    """
    opts = parse_args(args)
    doc = load(sys.stdin)
    opts.FORMAT(doc, sys.stdout)


def parse_args(args):
    p = argparse.ArgumentParser(description=main.__doc__)

    fmtp = p.add_mutually_exclusive_group()
    fmtp.set_defaults(
        FORMAT=dump_pretty,
    )
    fmtp.add_argument(
        '-p', '--pretty',
        dest='FORMAT',
        action='store_const',
        const=dump_pretty,
        help='Use pretty output format.',
    )

    fmtp.add_argument(
        '-c', '--compact',
        dest='FORMAT',
        action='store_const',
        const=dump_compact,
        help='Use compact output format.',
    )

    return p.parse_args(args)
