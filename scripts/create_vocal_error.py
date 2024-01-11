import os
import random
import re

def randomize_diacritics(text):
    diacritic_characters = ["َ", "ُ", "ِ", "ً", "ٌ", "ٍ"]
    randomized_text = ""

    for char in text:
        if char in diacritic_characters and random.choice([True, False]):
            randomized_text += random.choice(diacritic_characters)
        else:
            randomized_text += char

    return randomized_text

def process_files(folder_path):
    folder_path = folder_path.rstrip("/") + "/"

    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)

            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read()

            randomized_text = randomize_diacritics(text)

            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(randomized_text)

if __name__ == "__main__":
    folder_path = 'high_vocalized_error'
    process_files(folder_path)
