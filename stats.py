def get_num_words(path):
    try:
        word_count = -1
        with open(path, 'r') as f:
            print(f"Analyzing book found at {path}...")
            contents = f.read()
            words = contents.split()
            word_count = len(words)
            print("----------- Word Count ----------")
            print(f"Found {word_count} total words")
    except FileNotFoundError:
        print("Error: File not found.")

def to_list(chars):
    list_rep = []
    for char in chars:
        if char.isalpha():    
            list_rep.append({"char": char, "num": chars[char]})
    list_rep.sort(reverse=True, key=sort_on)
    return list_rep

def get_char_count(path):
    try:
        with open(path, 'r') as f:
            print("--------- Character Count -------")
            contents = f.read().lower()
            chars = {}
            for char in contents:
                if char in chars:
                    chars[char] += 1
                else:
                    chars[char] = 1
            return to_list(chars)
            
    except FileNotFoundError:
        print("Error: File not found.")

def sort_on(chars):
    return chars["num"]

def report(list_rep):
    for item in list_rep:
        print(f"{item["char"]}: {item["num"]}")