from stats import word_count_func, char_count_func

with open("books/frankenstein.txt") as f:
    contents = f.read()
def main():
    word_count_func(contents)
    char_count_func(contents)
main()