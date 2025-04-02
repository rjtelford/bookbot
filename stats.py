def get_number_words(words):
    return len(words.split())

def get_number_chars(book):
    character_dic = {}

    for char in book:
        if char.lower() in character_dic:
            character_dic[char.lower()] += 1
        else:
            character_dic[char.lower()] = 1

    return character_dic

def sort_on(dict):
    return dict["count"]

def sort_list(list):
    list.sort(reverse=True, key=sort_on)
    return list