import random

def random_vietnamese_word_generator(num_chars, word_type):
    # Sample Vietnamese words categorized by type
    nouns = ["bàn", "ghế", "nhà", "cây", "sách", "xe", "hoa", "trời", "biển"]
    verbs = ["đi", "chạy", "học", "viết", "ăn", "uống", "ngủ", "yêu", "nghĩ"]
    adjectives = ["đẹp", "xấu", "cao", "thấp", "nhanh", "chậm", "to", "nhỏ", "đỏ"]

    # Selecting the word list based on the type
    if word_type == "noun":
        word_list = nouns
    elif word_type == "verb":
        word_list = verbs
    elif word_type == "adjective":
        word_list = adjectives
    else:
        print("Invalid word type. Please choose 'noun', 'verb', or 'adjective'.")
        return

    # Filtering words based on the number of characters
    filtered_words = [word for word in word_list if len(word) == num_chars]
    
    if not filtered_words:
        print(f"No {word_type}s found with {num_chars} characters.")
        return

    # Randomly selecting a word
    random_word = random.choice(filtered_words)
    print(f"Generated {word_type}: {random_word}")

# User input
if __name__ == "__main__":
    try:
        num_chars = int(input("Enter the number of characters for the word: "))
        word_type = input("Enter the type of word (noun, verb, adjective): ").strip().lower()
        random_vietnamese_word_generator(num_chars, word_type)
    except ValueError:
        print("Please enter a valid number for the number of characters.")
