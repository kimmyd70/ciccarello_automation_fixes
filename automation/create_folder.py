from rich.console import Console
from rich.prompt import Prompt
import sys
import os

console = Console()
prompt = Prompt()

console.print("Would you like to create a folder?")

def make_folder():
  """Main function to run the CLI app."""
if os.path.exists('test_dir'):
  print(f'The directory already exists')
else:
  os.mkdir('test_dir')
  print(f'[bold blue]Directory Created[/bold blue]')


    


if __name__ == '__main__':
  name = Prompt.ask('What is your filename?', default='no')



# console = Console()
# # Create a source directory and a file inside it
# # Note the use of mkdirs and not mkdir here.
# # Use ChatGPT to show us the difference.
# os.makedirs('src_directory', exist_ok=True)
# with open('src_directory/src_file.txt', 'w') as f:
#     f.write('This is a demo file')
# # Create a destination directory
# os.makedirs('dst_directory', exist_ok=True)
# # Print contents of the directories before the move
# console.print("Before move operation")
# console.print("Contents of source directory:", os.listdir('src_directory'))
# console.print("Contents of destination directory:", os.listdir('dst_directory'))
# # Use shutil.move() to move the file
# shutil.move('src_directory/src_file.txt', 'dst_directory')
# # Print contents of the directories after the move
# console.print("After move operation")
# console.print("Contents of source directory:", os.listdir('src_directory'))
# console.print("Contents of destination directory:", os.listdir('dst_directory'))