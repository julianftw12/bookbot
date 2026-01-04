from stats import word_count_func, char_count_func, get_integer, sort_dict, print_items
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
book_path = sys.argv[1]

with open(f"{book_path}") as f:
    contents = f.read()
def main():
    word_count_func(contents)
    char_count_func(contents)
    sort_dict(char_count_func(contents))
    print(f"""
    ============ BOOKBOT ============
    Analyzing book found at {book_path}...
    ----------- Word Count -----------
    Found {word_count_func(contents)} total words
    --------- Character Count -------
    """)
    print_items(sort_dict(char_count_func(contents)))
main()