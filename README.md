# CodeAlpha_Task-Automation
This project is a simple Python automation task

# CodeAlpha Internship – Task 3  
## 🧩 Automation Script  
### 👤 Created By: **Radhika Sharma**

---

## 📌 Overview  
This project is part of the **CodeAlpha Python Internship – Task 3**.  
The goal of this task is to **automate a simple process using Python**.  
I built a script that **automatically moves specific file types** (such as PNG images) from one folder to another.

This automation helps in reducing manual work and keeping files well organized.

---

## 💡 What This Script Does  
✔ Reads all files from a source folder  
✔ Checks if the file ends with `.png`  
✔ Creates the destination folder (if it does not already exist)  
✔ Moves each matching file to the new folder  
✔ Shows a success message for every file moved  

---

## 🛠 Technologies Used  
- **Python**
- `os` module  
- `shutil` module  

---

## 📂 File Organization Flow  
**Source Folder ➝ Python Script ➝ Destination Folder**

Example:  
All `.png` images from  
`C:\Users\DELL\Videos\Captures`  
are moved to  
`C:\Users\DELL\Music\New folder`

---

## 🧠 Skills Learned  
- File handling  
- Basic automation  
- Working with modules (`os`, `shutil`)  
- Understanding paths  
- Conditional checks in Python  

---

## 📜 Code Used

```python
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
    if file_name.lower().endswith(".png"):
        full_path = os.path.join(source, file_name)
        new_path = os.path.join(destination, file_name)
        shutil.move(full_path, new_path)
        print(f"{file_name} moved successfully!")

print("All PNG files have been moved successfully!")

