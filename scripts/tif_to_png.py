from PIL import Image
import os

def convert_tiff_to_png(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".tif") or filename.endswith(".tiff"):
            tiff_filepath = os.path.join(folder_path, filename)
            png_filepath = os.path.splitext(tiff_filepath)[0] + ".png"

            try:
                # Open the TIFF file and save it as PNG
                with Image.open(tiff_filepath) as img:
                    img.save(png_filepath, format="PNG")
                print(f"Converted {filename} to {os.path.basename(png_filepath)}")
            except Exception as e:
                print(f"Error converting {filename}: {str(e)}")

if __name__ ==  "__main__":
    folder_path = 'examples'  # Replace with the path to your folder containing TIFF files
    convert_tiff_to_png(folder_path)
