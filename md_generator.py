import hashlib


def md_gen(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            yield hashlib.md5(line.encode())