def read_file(file_path: str) -> str:
    with open(file_path, 'r') as file:
        return file.read()

def write_file(file_path: str, content: str):
    with open(file_path, 'w') as file:
        file.write(content)

def append_file(file_path: str, content: str):
    with open(file_path, 'a') as file:
        file.write(content)

def count_lines_in_file(file_path: str) -> int:
    with open(file_path, 'r') as file:
        return len(file.readlines())

def file_exists(file_path: str) -> bool:
    try:
        with open(file_path, 'r'):
            return True
    except FileNotFoundError:
        return False
