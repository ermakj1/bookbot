import sys
from stats import get_num_words
from stats import get_char_count
from stats import get_sorted_dict

def get_book_text(filepath):
    text = "Empty"
    with open(filepath, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

def print_char_info(dict):
    if dict["char"].isalpha():
        print(f"{dict['char']}: {dict['num']}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    book_text = get_book_text(filepath)
    word_count = get_num_words(book_text)
    char_count = get_char_count(book_text)
    sorted_dict = get_sorted_dict(char_count)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char in sorted_dict:
        print_char_info(char)
    print("============= END ===============")


main()