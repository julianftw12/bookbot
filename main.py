from stats import word_count_func

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        contents = f.read()
    return contents

def main():
    word_count_func(get_book_text("books/frankenstein.txt"))
main()