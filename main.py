import ast
import sys

TARGET_FILE = sys.argv[1] if len(sys.argv) > 1 else "target.py"

def find_defined_function_call(tree, rules, filename):
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            for rule in rules:
                rule(node, filename)


def find_popen_uses(node, filename):
    try:
        # Check for module name == subprocess
        if not (module_name := node.func.value.id) or module_name != "subprocess":
            return None
        
        # Check for function name == Popen
        if not (func_name := node.func.attr) or func_name != "Popen":
            return None

        if not (keywords := node.keywords):
            return None
        
        shell_arg = False

        for keyword in keywords:
            if not keyword.arg or keyword.arg != "shell":
                continue
            if not keyword.value or not keyword.value.value:
                continue

            shell_arg = True
        
        if not shell_arg:
            return None

        if not (func_args := node.args) or isinstance(func_args[0], ast.Constant):
            return None

        print(f"Insecure use of {module_name} found @ line {node.lineno} in {filename}")
    except:
        return None
    

def main():
    with open(TARGET_FILE, "r") as file:
        content = file.read()

    parsed_ast = ast.parse(content)
    
    find_defined_function_call(parsed_ast, [find_popen_uses], TARGET_FILE)
    

if __name__ == "__main__":
    main()