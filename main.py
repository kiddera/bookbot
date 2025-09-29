from stats import count_words, count_chars, sortit
import sys

def get_book_text(filepath):
    contents = ""
    with open(filepath) as reader:
        contents = reader.read()
    return contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    text = get_book_text(path)
    nw = count_words(text)
    cc = count_chars(text)
    lcc = sortit(cc)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {nw} total words")
    print("--------- Character Count -------")
    for entry in lcc:
        if not entry["char"].isalpha():
            continue
        print(f"{entry["char"]}: {entry["num"]}")
    print("============= END ===============")

main()
