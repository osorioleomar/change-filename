import os
import re

# Set the path to the folder containing the image files
folder_path = '/path/to/your/folder'

# Function to remove special characters
def remove_special_chars(filename):
    # The regular expression pattern allows letters, numbers, periods, and spaces
    pattern = re.compile(r'[^a-zA-Z0-9\.\s]+')
    return pattern.sub('', filename)

# Iterate through the files in the folder
for old_filename in os.listdir(folder_path):
    # Check if the file is an image (you may add more extensions as needed)
    if old_filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff')):
        # Remove special characters from the filename
        new_filename = remove_special_chars(old_filename)
        
        # Rename the file if the new name is different from the old name
        if new_filename != old_filename:
            old_filepath = os.path.join(folder_path, old_filename)
            new_filepath = os.path.join(folder_path, new_filename)
            os.rename(old_filepath, new_filepath)
            print(f'Renamed: {old_filename} -> {new_filename}')
