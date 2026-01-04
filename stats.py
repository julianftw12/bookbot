def word_count_func(contents):
    words = contents.split()
    num_words = len(words)
    return num_words

def char_count_func(contents):
    lowercase = contents.lower()
    chars = {}
    for char in lowercase:
        if char in chars:
            chars[char] += 1
        elif char.isalpha() != True:
            pass
        else:
           chars[char] = 1
    return(chars)

def get_integer(entry):
    return entry["Integer"]

def sort_dict(original_dict):
    sorted_list = sorted(
        [{"Letter" : letter , "Integer" : integer} for letter , integer in original_dict.items()],
        key = get_integer,
        reverse = True
    )
    return sorted_list
def print_items(sorted_list):
    for entry in sorted_list:
        print(f"{entry['Letter']}: {entry['Integer']}")