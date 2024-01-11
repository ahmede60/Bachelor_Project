import os
import random

def introduce_errors(file_path):
    with open(file_path, 'r', encoding='utf-8') as input_file:
        original_text = input_file.read()

    modified_text = list(original_text)
    line_break_indices = [i for i, char in enumerate(modified_text) if char == '\n']

    for i in range(4, len(original_text), 5):  # Change 19 and 20 for every 20 characters
        if i < len(modified_text):
            random_index = random.randint(i - 5, i)
            # Replace with a random Arabic character from the given list
            modified_text[random_index] = random.choice(arabic_characters)

    # Restore line breaks
    for index in line_break_indices:
        modified_text[index] = '\n'

    with open(file_path, 'w', encoding='utf-8') as output_file:
        output_file.write(''.join(modified_text))

if __name__ == "__main__":
    # Specify the folder containing text files
    folder_path = '/home/ocr_project/five_char_error'

    # List of Arabic alphabets
    arabic_characters = 'ابتثجحخدذرزسشصضطظعغفقكلمنهوي'

    # Iterate over each text file in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            file_path = os.path.join(folder_path, filename)
            introduce_errors(file_path)

    print("Modification completed.")
