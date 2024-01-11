import os

def delete_lstmf_files(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".box"):
            file_path = os.path.join(folder_path, filename)
            try:
                os.remove(file_path)
                print(f"Deleted: {filename}")
            except Exception as e:
                print(f"Error deleting {filename}: {e}")

if __name__ == "__main__":
    # Specify the folder containing .lstmf files
    folder_path = '/home/ocr_project/tesstrain/data/ground-truth'

    delete_lstmf_files(folder_path)
