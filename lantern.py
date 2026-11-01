import argparse
from tasks import list_tasks

parser = argparse.ArgumentParser()
sub = parser.add_subparsers(dest="cmd")
sub.add_parser("add")
list_parser = sub.add_parser("list")
list_parser.add_argument("--sort", action="store_true")
args = parser.parse_args()

if args.cmd == "list":
    for task in list_tasks(sort_by_title=args.sort):
        print(task["title"])
else:
    print(f"Running {args.cmd}")