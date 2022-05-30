import sys 
from glob import glob

def get_dynamic_modules(path: list):
    modules = []

    for command in path:
        sys.path.append(command)
        for file in glob(f'{command}*.py'):
            if file.endswith('__.py'):
                continue
            file = file.replace(f'{command}', '').replace('.py', '')
            modules.append(file)

    return modules