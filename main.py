def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    counted_characters = count_characters(text)
    alphabetic_characters = filter_alphabetic_characters(counted_characters)
    list_of_dicts = convert_to_list_of_dicts(alphabetic_characters)
    list_of_dicts.sort(reverse=True, key=sort_on)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")
    for item in list_of_dicts:
        print(f"The '{item['character']}' character was found {item['num']} times")
    print("--- End report ---")

#convert into a list of dictionaries
def convert_to_list_of_dicts(alphabetic_characters):
    list_of_dicts = []
    for character, count in alphabetic_characters.items():
        list_of_dicts.append({"character": character, "num": count})
    return list_of_dicts


def sort_on(dict):
    return dict["num"]



#filter out non-alphabetic characters
def filter_alphabetic_characters(counted_characters):
    alphabetic_characters = {}
    for key in counted_characters:
        if key.isalpha() == True:
            alphabetic_characters[key] = counted_characters[key]
    return alphabetic_characters
            
    

# returns the number of times each character appears
def count_characters(text):
    counted_characters = {}
    # convert any character to lowercase
    lowered_text = text.lower()
    for character in lowered_text:
        if character in counted_characters:
            counted_characters[character] += 1
        else: counted_characters[character] = 1
    return counted_characters


# reads the book
def get_book_text(path):
    with open(path) as f:
        return f.read()
    
# counts the words
def count_words(text):
    return len(text.split())


main()