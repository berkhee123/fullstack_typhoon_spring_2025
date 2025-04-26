# file_utils.py

def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()

def write_file(filename, content):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)

def append_file(filename, content):
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(content)

def count_lines(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return len(file.readlines())

def count_words(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
        words = text.split()
        return len(words)

def search_text(filename, search_term):
    found_lines = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            if search_term in line:
                found_lines.append(line.strip())
    return found_lines
