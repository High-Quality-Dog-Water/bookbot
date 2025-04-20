from stats import get_num_words, sort_dict_by_value, get_num_characters
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    letter_dict = get_num_characters(text)
    letter_dict = sort_dict_by_value(letter_dict)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char, count in letter_dict:
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
