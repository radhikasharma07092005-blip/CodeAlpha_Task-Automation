import os
import shutil

# Correct source and destination paths
source = r"C:\Users\DELL\Videos\Captures"
destination = r"C:\Users\DELL\Music\New folder"

# Create destination folder if it doesn't exist
if not os.path.exists(destination):
    os.makedirs(destination)

# Move all .png files
for file_name in os.listdir(source):
    if file_name.lower().endswith(".png"):  # move .png files
        full_path = os.path.join(source, file_name)
        new_path = os.path.join(destination, file_name)
        shutil.move(full_path, new_path)
        print(f"{file_name} moved successfully!")

print("All PNG files have been moved successfully!")
