import ast
import sys
import os

from ast_logic import find_defined_function_call, find_popen_uses


def scan_single_file(filename):
    with open(filename, "r") as file:
        content = file.read()
    
    parsed_ast = ast.parse(content)
    
    find_defined_function_call(parsed_ast, [find_popen_uses], filename)


def scan_multiple_files(dir):
    pass


def main():
    if len(sys.argv) < 2:
        print("Error: Missing argument")
        exit(-1)

    target = sys.argv[1]

    if os.path.isdir(target):
        scan_multiple_files(target)
    else:
        scan_single_file(target)
        

if __name__ == "__main__":
    main()