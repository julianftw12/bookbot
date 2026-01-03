def word_count_func(contents):
    words = contents.split()
    num_words = len(words)
    print(f"Found {num_words} total words")

def char_count_func(contents):
    lowercase = contents.lower()
    chars = {}
    for char in lowercase:
        if char in chars:
            chars[char] += 1
        else:
           chars[char] = 1
    print(chars)
