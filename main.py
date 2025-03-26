import sys
from stats import get_ch_count, sort_char_count, get_num_words

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    filepath = sys.argv[1]
    text = get_book_text(filepath)
    counts = get_ch_count(text)
    sorted_count = sort_char_count(counts)
    total_words = get_num_words(text)

    print("============ BOOKBOT =============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count -----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count --------")

    for item in sorted_count:
        print(f"{item['char']}: {item['count']}")

    print("============= END ================")

def get_book_text(filepath):
    try:
        with open(filepath) as f:
            return f.read()
    except PermissionError:
        print(f"Error: Permission denied when reading {filepath}")
        sys.exit(1)
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        sys.exit(1)

if __name__ == "__main__":
    main()
