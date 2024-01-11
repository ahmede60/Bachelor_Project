import os
import random
import re

def add_random_vocalization(text):
    # Define Arabic diacritic characters representing short vowels
    vocalization_characters = ["َ", "ُ", "ِ", "ً", "ٌ", "ٍ"]

    # Add random vocalization characters to the text
    vocalized_text = ""
    for char in text:
        vocalized_text += char
        if char.strip() and random.choice([True, False]):
            vocalized_text += random.choice(vocalization_characters)

    return vocalized_text

def process_files(folder_path):
    # Ensure the folder path ends with a slash
    folder_path = folder_path.rstrip("/") + "/"

    # Loop through each text file in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)

            # Read the content of the file
            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read()

            # Add random vocalization characters
            vocalized_text = add_random_vocalization(text)

            # Write the vocalized text back to the file
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(vocalized_text)

if __name__ == "__main__":
    # Replace 'your_folder_path' with the actual path to your folder containing text files
    folder_path = 'high_diacritics_evaluation/'

    # Process text files in the specified folder
    process_files(folder_path)

