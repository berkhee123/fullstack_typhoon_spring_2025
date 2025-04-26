# test_file_utils.py

import file_utils

def test_file_utils():
    test_filename = 'test_file.txt'

    # Тест 1: write_file ба read_file
    file_utils.write_file(test_filename, "Hello world!\nWelcome to Python testing.")
    content = file_utils.read_file(test_filename)
    assert content == "Hello world!\nWelcome to Python testing.", "write_file эсвэл read_file буруу байна."

    # Тест 2: append_file
    file_utils.append_file(test_filename, "\nLet's append this line.")
    content = file_utils.read_file(test_filename)
    assert "Let's append this line." in content, "append_file ажиллахгүй байна."

    # Тест 3: count_lines
    lines_count = file_utils.count_lines(test_filename)
    assert lines_count == 3, f"count_lines буруу байна. Одоогийн мөр: {lines_count}"

    # Тест 4: count_words
    words_count = file_utils.count_words(test_filename)
    assert words_count == 10, f"count_words буруу байна. Одоогийн үгсийн тоо: {words_count}"

    # Тест 5: search_text
    found_lines = file_utils.search_text(test_filename, "Python")
    assert any("Python" in line for line in found_lines), "search_text ажиллахгүй байна."

    print("Бүх тестүүд амжилттай боллоо!")

if __name__ == "__main__":
    test_file_utils()
