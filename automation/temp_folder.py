from rich.console import Console
from rich.prompt import Prompt
import shutil
import os

console = Console()

def make_temp_folder():
    # this creates a folder temp
  if os.path.exists('temp'):
    print(f'The directory already exists')
  else:
    os.mkdir('temp')
    console.print(f'Directory Created')
    move_file()

  # This moves files to the newly created temp folder. When the files are moved, they are essentially deleted and copied to the new folder
def move_file():
  shutil.move('user2/document2.txt', 'temp')
  shutil.move('user2/email2.mail', 'temp')




if __name__ == '__main__':
  name = Prompt.ask('Would you like to make a temporary folder?', default='no').lower()
  # if name == 'y' or 'Y' or 'yes' or 'YES': 
  make_temp_folder()