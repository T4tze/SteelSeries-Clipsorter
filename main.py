import os
import shutil

main_folder = r"E:\Clips\GG"

video_extensions = (".mp4", ".mov", ".mkv")

for file in os.listdir(main_folder):
    file_path = os.path.join(main_folder, file)

    if os.path.isdir(file_path):
        continue

    if file.lower().endswith(video_extensions):
        if "_" in file:
            folder_name = file.split("_")[0]
        else:
            continue

        target_folder = os.path.join(main_folder, folder_name)

        if not os.path.exists(target_folder):
            os.makedirs(target_folder)

        shutil.move(file_path, os.path.join(target_folder, file))
