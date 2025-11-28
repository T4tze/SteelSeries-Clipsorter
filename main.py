import os
import shutil

main_folder = r"E:\Clips\GG" # Folder where you put your clips
video_extensions = (".mp4", ".mov", ".mkv")

try:
    files = os.listdir(main_folder)
except Exception as e:
    print("Failed to list directory:", e)
    raise SystemExit

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
