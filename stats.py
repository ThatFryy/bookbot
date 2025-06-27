# Insert function below

def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    text = text.lower()
    chars = {}    
    for char in text:
            if char in chars:
                chars[char] += 1
            else:
                chars[char] = 1
    return chars

def sort_char_count(chars):
    char_list = [{"char": c, "num": n} for c, n in chars.items()]
    char_list.sort(reverse=True, key=lambda item: item["num"])
    
    return char_list