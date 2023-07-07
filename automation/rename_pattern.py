import os


def rename_files_with_pattern(folder_path, old_pattern, new_pattern):
    # Get a list of files in the folder
    files = os.makedirs(folder_path)

    # Iterate over the files
    for file in files:
        # Check if the file matches the old pattern
        if old_pattern in file:
            # Create the new file name by replacing the old pattern with the new pattern
            new_file_name = file.replace(old_pattern, new_pattern)

            # Construct the full paths for the old and new files
            old_file_path = os.path.join(folder_path, file)
            new_file_path = os.path.join(folder_path, new_file_name)

            # Rename the file
            os.rename(old_file_path, new_file_path)
            print(f"Renamed '{file}' to '{new_file_name}'")


if __name__ == "__main__":
    # Specify the folder path, old pattern, and new pattern
    folder_path = "Automation/User1"  # Replace with the actual folder path
    old_pattern = "1"  # Replace with the pattern you want to replace
    new_pattern = "2"  # Replace with the new pattern you want to use

    # Call the function to rename the files
    rename_files_with_pattern(folder_path, old_pattern, new_pattern)



# Needs to be reworked