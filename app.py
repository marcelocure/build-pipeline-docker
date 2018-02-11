import argparse
import sys
from docker_build import build_and_push

def parse_args(argv):
    arg_parser = argparse.ArgumentParser(
        prog=argv[0],
        formatter_class=argparse.RawDescriptionHelpFormatter)
    arg_parser.add_argument('name')
    return arg_parser.parse_args()

def main(argv):
    args = parse_args(argv)
    build_and_push(name=args.name)

if __name__ == "__main__":
    main(sys.argv)