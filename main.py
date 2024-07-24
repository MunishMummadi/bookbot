def main():
    file_path = "books/frankenstein.txt"
    text = get_text_from_book(file_path)
    word_count = get_word_count(text)
    char_count = get_char_count(text)
    print(f"--- Begin report of {file_path} ---")
    print(f"{word_count} words found in the document")
    for char,count in char_count.items():
        if char.isalpha():
            print(f"The '{char}' character was found {count} times")
    print("--- End report ---")


def get_text_from_book(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    test_list = text.split()
    return len(test_list)

def get_char_count(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] +=1
        else:
            chars[lowered] = 1
    return chars


main()