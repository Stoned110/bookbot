def get_num_words(text):
    word_list = text.split()
    words_count = len(word_list)
    return words_count

def get_ch_count(text):
    text = text.lower()  
    counts = {}          
    
    for char in text:
        if char.isalpha():  
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1
    
    return counts  

def sort_char_count(counts):
    sorted_list = [{"char": char, "count": count} for char, count in counts.items() if char.isalpha()]
    sorted_list.sort(key=lambda x: x["count"], reverse=True)
    return sorted_list

