import sys
import argparse


def main(args=sys.argv[1:]):
    """
    Check a JSON input for safety problems.
    """
    opts = parse_args(args)
    raise NotImplementedError((main, opts))


def parse_args(args):
    p = argparse.ArgumentParser(description=main.__doc__)
    return p.parse_args(args)
