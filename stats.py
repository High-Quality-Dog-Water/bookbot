def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_characters(text):
    letter_count_dict = {}
    char = text
    for letter in char:
        letter = letter.lower()
        if letter not in letter_count_dict:
            letter_count_dict[letter] = 1
        else:
            letter_count_dict[letter] += 1
            
    return letter_count_dict

def sort_dict_by_value(letter_count_dict):
    dict_list = []
    for key, value in letter_count_dict.items():
        dict_list.append((key, value))
    dict_list.sort(reverse=True, key=lambda x: x[1])
    return dict_list