import argparse
import os
from datetime import datetime

parser = argparse.ArgumentParser()

parser.add_argument("-f", action="store")
parser.add_argument("-d", action="store", nargs="*")

args = parser.parse_args()

if args.f is None and args.d is None:
    raise SystemExit("You cannot specified any arguments")

if args.d is not None:
    path = os.path.join(os.curdir, *args.d)
    if not os.path.exists(path):
        os.makedirs(path)
    os.chdir(path)

if args.f is not None:
    with open(args.f, "a") as file:
        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))
        line_number = 1
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            file.write(f"{line_number} {line}\n")
            line_number += 1
        file.write("\n")
