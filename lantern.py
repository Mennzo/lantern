import argparse

parser = argparse.ArgumentParser()
sub = parser.add_subparsers(dest="cmd")
sub.add_parser("add")
list_parser = sub.add_parser("list")
list_parser.add_argument("--done", action="store_true")
args = parser.parse_args()
print(f"Running {args.cmd}")
