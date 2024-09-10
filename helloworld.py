import sys
# Assignment 2

if len(sys.argv) < 2:
    print("Usage: python helloWorld.py <name>")
else:
    name = " ".join(sys.argv[1:])
    print(f"Hello, {name}!")