import sys
from stats import get_number_words
from stats import get_number_chars
from stats import sort_list

def get_book_text(book_location):
    with open(book_location) as book:
        return book.read()
    

    

def main():
    
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    else:
    
        book_title_location = sys.argv[1]
        book_text = get_book_text(book_title_location)
        num_words = get_number_words(book_text)
        character_dic = get_number_chars(book_text)
        
        character_list = []

        for item in character_dic:
            dict  = {}
            dict["char"] = item
            dict["count"] = character_dic[item]
            character_list.append(dict)


        print("============ BOOKBOT ============")
        print("Analyzing book found at " + book_title_location + "...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")

        for item in sort_list(character_list):
            if item["char"].isalpha():
                print(f"{item["char"]}: {item["count"]}")

        print("============= END ===============")
    
    
main()
