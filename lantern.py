import argparse

parser = argparse.ArgumentParser()
sub = parser.add_subparsers(dest="cmd")
sub.add_parser("add")
list_parser = sub.add_parser("list")
args = parser.parse_args()
print(f"Running {args.cmd}")
