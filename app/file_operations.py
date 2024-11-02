""" asd """


def read_file(file_path: str) -> str:
    """ asd """
    with open(file_path, 'r', encoding='utf-8')as file:
        return file.read()


def write_file(file_path: str, content: str):
    """ asd """

    with open(file_path, 'r', encoding='utf-8') as file:
        file.write(content)


def append_file(file_path: str, content: str):
    """ asd """

    with open(file_path, 'r', encoding='utf-8') as file:
        file.write(content)


def count_lines_in_file(file_path: str) -> int:
    """ asd """

    with open(file_path, 'r', encoding='utf-8') as file:
        return len(file.readlines())


def file_exists(file_path: str) -> bool:
    """ asd """

    try:
        with open(file_path, 'r', encoding='utf-8'):
            return True
    except FileNotFoundError:
        return False
