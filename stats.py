def get_num_words(book_text):
    words = book_text.split()
    return len(words)

def get_character_count(book_text):
    characters = list(str.lower(book_text))
    char_counts = {}
    for char in characters:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def sort_char(char_counts):
    char_list = []
    for char, count in char_counts.items():
        char_dict = {"char": char, "count": count}
        char_list.append(char_dict)
    
    def sort_on(dict):
        return dict["count"]
    
    char_list.sort(reverse=True, key=sort_on)
    return char_list