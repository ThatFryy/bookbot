import sys
from stats import count_words, count_chars, sort_char_count


def get_book_text(path):
    with open(path) as f:
        return f.read()


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    path = sys.argv[1]

    print("========== BOOKBOT ==========")
    print(f"Analyzing book found at {path}...")
    
    text = get_book_text(path)
    num_words = count_words(text)
    chars = count_chars(text)
    sorted_chars = sort_char_count(chars)
    
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    
    print("--------- Character Count -------")
    for item in sorted_chars:
        char = item["char"]
        num = item["num"]
        if char.isalpha():
            print(f"{char}: {num}")
        
main()