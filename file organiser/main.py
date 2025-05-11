import os
import shutil

downloads_folder = os.path.expanduser("~/Downloads")
desktop_folder = os.path.expanduser("~/Desktop")
documents_folder = os.path.expanduser("~/Documents")

file_types = {
    '.Images': ['.jpg', '.png', '.gif', '.bmp', '.webp'],
    '.Videos': ['.mp4', '.mov', '.mkv', '.avi'],
    '.Audio': ['.mp3', '.ogg', '.wav'],
    '.Docs': ['.pdf', '.docx', '.txt', 'pptx', '.json'],
    '.Files': ['.exe', '.zip']
}

files = os.listdir(downloads_folder) + os.listdir(desktop_folder)
print(files)

def create_folder(name):
    folder_path = os.path.join(documents_folder, name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    return folder_path

def move_file(name, category, folder):
    source_path = os.path.join(folder, name)
    destination_folder = create_folder(category)
    destination_path = os.path.join(destination_folder, name)

    print(f"Source path: {source_path}")
    print(f"Destination path: {destination_path}")

    if not os.path.exists(source_path):
        print(f"File not found: {source_path}")
        return

    try:
        shutil.move(source_path, destination_path)
        print(f"Successfully moved {name} to {destination_path}")
    except Exception as e:
        print(f"Error moving {name}: {e}")

for folder in [downloads_folder, desktop_folder]:
    files_in_folder = os.listdir(folder)

    for file in files:
        extension = os.path.splitext(file)[1].lower()

        for category, extensions in file_types.items():
            if extension in extensions:
                move_file(file, category, folder)
                break
                #print(f"{file}, {category}")