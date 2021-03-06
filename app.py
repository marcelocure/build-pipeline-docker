import argparse
import sys
from docker_push import tag_and_push
from docker_build import run_build

def parse_args(argv):
    arg_parser = argparse.ArgumentParser(prog=argv[0])
    arg_parser.add_argument('name')
    return arg_parser.parse_args()

def main(argv):
    args = parse_args(argv)
    status = run_build(args.name)
    if status != 0:
        print "build failing"
        sys.exit(status)
    else:
        tag_and_push(name=args.name)

if __name__ == "__main__":
    main(sys.argv)