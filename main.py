import re

def main() -> None:
    path_to_file = r'books/frankenstein.txt'
    text = get_book_text(path_to_file)
    print(f"--- Begin report of {path_to_file} ---")

    print(f"{get_number_of_words(text)} words found in the document\n")

    number_of_characters = count_characters(text)
    reversed_order_num_of_char = reversed_order_by_value(number_of_characters)
    for letter, value in reversed_order_num_of_char.items():
        if is_letter(letter):
            print(f"The '{letter}' character was found {value} times")
    print("--- End report ---")
    
    
def get_book_text(path: str) -> str:
    with open(path) as f:
        return f.read()
    
def get_number_of_words(text: str) -> int:
    words = text.split()
    return len(words)

def count_characters(text: str) -> dict[str: int]:
    character_counts = {}
    for letter in text:
        lower_letter = letter.lower()
        if lower_letter not in character_counts:
            character_counts[lower_letter] = 1
        else:
            character_counts[lower_letter] += 1
    return character_counts

def reversed_order_by_value(dct: dict) -> dict:
    return dict(sorted(dct.items(), key=lambda item: item[1], reverse=True))

def is_letter(char: str) -> bool:
    return bool(re.search('[a-z]', char))

main()