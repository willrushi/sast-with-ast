import sys

from funcs import my_func

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error: No argument provided.")
        exit(-1)

    my_func(sys.argv[1])