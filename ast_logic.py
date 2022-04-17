import ast

def find_defined_function_call(tree, rules, filename):
    hits = []

    for node in ast.walk(tree):
        if isinstance(node, ast.Call):

            for rule in rules:
                if rule(node):
                    print(f"Found vuln @ line {node.lineno} in {filename}")


def find_popen_uses(node):
    try:
        # Check for module name == subprocess
        if not (module_name := node.func.value.id) or module_name != "subprocess":
            return False
        
        # Check for function name == Popen
        if not (func_name := node.func.attr) or func_name != "Popen":
            return False

        if not (keywords := node.keywords):
            return False
        
        shell_arg = False

        for keyword in keywords:
            if not keyword.arg or keyword.arg != "shell":
                continue
            if not keyword.value or not keyword.value.value:
                continue

            shell_arg = True
        
        if not shell_arg:
            return False

        if not (func_args := node.args) or isinstance(func_args[0], ast.Constant):
            return False

        return True
    except:
        return False