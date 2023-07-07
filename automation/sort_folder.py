from rich.prompt import Prompt
import shutil
import os

prompt = Prompt()

def sort_documents(folder_path):

    file_types = {
        '.txt': "logs",
        '.mail': "mail"
    }

    main_directory = os.path.dirname(folder_path)

    for file_extension, folder_name in file_types.items():
        destination_folder = os.path.join(main_directory, folder_name)
        os.makedirs(destination_folder, exist_ok=True)

    for file in os.listdir(folder_path):
        file_route = os.path.join(folder_path, file)

        if os.path.isfile(file_route):
            file_extension = os.path.splitext(file)[1]
            if file_extension in file_types:
                destination_folder = os.path.join(main_directory, file_types[file_extension])
                shutil.move(file_route, os.path.join(destination_folder, file))
                print(f"Moved {file} to {destination_folder} folder")


if __name__ == "__main__":
  folder_route = Prompt.ask('Enter parent folder to sort documents?')

  if os.path.exists(folder_route):
    sort_documents(folder_route)
  else:
    print('Directory excommunicado')

