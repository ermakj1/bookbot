
def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    char_count = {}
    text = text.lower()
    for char in text:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    return char_count

def sort_on(items):
    return items["num"]

def get_sorted_dict(dict):
    sorted = []
    for char in dict:
        letter = {"char": char, "num": dict[char]}
        sorted.append(letter)

    sorted.sort(reverse=True, key=sort_on)
    return sorted