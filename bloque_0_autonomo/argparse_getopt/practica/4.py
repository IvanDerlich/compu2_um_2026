import argparse

parser = argparse.ArgumentParser(description="verbosidad y silencio")

group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", action="store_true")
group.add_argument("-q", "--quiet", action="store_true")

args = parser.parse_args()

if args.verbose:
    print("Verbose mode is on")
elif args.quiet:
    print("Quiet mode is on")
else:
    print("Normal mode")