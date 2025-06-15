from stats import get_num_words, get_char_count, report
from sys import argv, exit

def main():
    if len(argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)
    print("============ BOOKBOT ============")
    for path in argv:
        if path == "main.py":
            continue
        get_num_words(path)
        list_rep = get_char_count(path)
        report(list_rep)
        print("============= END ===============")

main()