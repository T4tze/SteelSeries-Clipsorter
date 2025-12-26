import os
import shutil

main_folder = r"E:\Clips\GG" # Folder where you put your clips
video_extensions = (".mp4", ".mov", ".mkv")

def sort():
    try:
        files = os.listdir(main_folder)
    except Exception as e:
        print("Failed to list directory:", e)
        return

    for file in files:
        file_path = os.path.join(main_folder, file)

        try:
            if os.path.isdir(file_path):
                print("Skipping folder:", file)
                continue

            if not file.lower().endswith(video_extensions):
                print("Not a video:", file)
                continue

            if "_" not in file:
                print("No underscore found:", file)
                continue

            folder_name = file.split("_")[0]
            target_folder = os.path.join(main_folder, folder_name)

            if not os.path.exists(target_folder):
                try:
                    os.makedirs(target_folder)
                    print("Created folder:", target_folder)
                except Exception as e:
                    print("Failed to create folder:", target_folder, e)
                    continue

            try:
                shutil.move(file_path, os.path.join(target_folder, file))
                print("Moved:", file, "->", target_folder)
            except Exception as e:
                print("Failed to move file:", file, e)

        except Exception as e:
            print("Error processing file:", file, e)


def back():

    try:
        folders = [d for d in os.listdir(main_folder)
                   if os.path.isdir(os.path.join(main_folder, d))]
    except Exception as e:
        print("Failed to list subfolders:", e)
        return

    for folder in folders:
        folder_path = os.path.join(main_folder, folder)

        try:
            subfiles = os.listdir(folder_path)
        except Exception as e:
            print("Failed to list folder:", folder, e)
            continue

        for file in subfiles:
            src = os.path.join(folder_path, file)
            dst = os.path.join(main_folder, file)

            if not file.lower().endswith(video_extensions):
                continue

            try:
                shutil.move(src, dst)
                print(f"Moved back: {file}")
            except Exception as e:
                print(f"Failed to move back {file}:", e)

print("What do you wanna do?")
print("1 = Sort (Clips into folders)")
print("2 = back (Clips into main folder)")

aktion = input("Pick: ").strip().lower()

if aktion == "1" or aktion == "back":
    sort()
elif aktion == "2" or aktion == "sort":
    back()
else:
    print("Error.")
