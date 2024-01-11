import os
import random

def swap_characters(text):
    # Define the characters to swap
    swap_mapping = {
        'ا': 'ل', 'ل': 'ا', 'ف': 'ق', 'ق': 'ف', 'ب': 'ي', 'ي': 'ب',
        'ن': 'ث', 'ث': 'ن', 'ت': 'ن', 'ن': 'ت', 'ت': 'ث', 'ث': 'ت', 'ج': 'خ', 'خ': 'ج', 'ح': 'خ',
        'خ': 'ح', 'ج': 'ح', 'ح': 'ج', 'ص': 'ض', 'ض': 'ص', 'س': 'ش', 'ش': 'س', 'ع': 'غ',
        'غ': 'ع', 'ط': 'ظ', 'ظ': 'ط', 'د': 'ذ', 'ذ': 'د', 'ر': 'ز', 'ز': 'ر', 'ه': 'م', 'م': 'ه'
    }
    
    modified_text = ''
    for char in text:
        # Randomly decide whether to swap with a probability of 0.1 (10%)
        if char in swap_mapping and random.random() < 0.067:
            modified_text += swap_mapping[char]
        else:
            modified_text += char

    return modified_text

def process_files(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            filepath = os.path.join(folder_path, filename)

            with open(filepath, 'r', encoding='utf-8') as file:
                text = file.read()

            modified_text = swap_characters(text)

            with open(filepath, 'w', encoding='utf-8') as file:
                file.write(modified_text)

if __name__ == "__main__":
    folder_path = 'fifteen_similar_char_error'  # Replace with the path to your folder containing text files

    process_files(folder_path)
