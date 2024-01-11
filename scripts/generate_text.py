import random
import string

def generate_arabic_text_file(output_file_path, num_lines, chars_per_line=10):
    arabic_characters = 'ابتثجحخدذرزسشصضطظعغفقكلمنهوي'
    
    with open(output_file_path, 'w', encoding='utf-8') as file:
        for _ in range(num_lines):
            line = ''.join(random.choice(arabic_characters) for _ in range(chars_per_line))
            file.write(line + ' ')
            if (_ + 1) % 10 == 0:
                file.write('\n')

# Specify the output file path and the number of lines (10,000)
output_file_path = "evaluation/ah.txt"
num_lines = 100

# Generate the text file
generate_arabic_text_file(output_file_path, num_lines)

print(f"Text file generated: {output_file_path}")

