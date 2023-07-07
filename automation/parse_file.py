from rich.console import Console
from rich.prompt import Prompt
import os

console = Console()

def parse_log_file(log_file_path, target_directory):
    os.makedirs(target_directory, exist_ok=True)
    errors_log_file = os.path.join(target_directory, "errors.log")
    warnings_log_file = os.path.join(target_directory, "warnings.log")

    with open(log_file_path, 'r') as log_file:
        lines = log_file.readlines()

    errors = [line for line in lines if "ERROR" in line]
    warnings = [line for line in lines if "WARNING" in line]

    with open(errors_log_file, 'w') as errors_file:
        errors_file.writelines(errors)

    with open(warnings_log_file, 'w') as warnings_file:
        warnings_file.writelines(warnings)

    console.print("Log file parsed successfully!", style="bold green")



if __name__ == "__main__":
# Prompt for the log file path and target directory
  log_file_path = Prompt.ask("Enter the path to the log file: ")
  target_directory = Prompt.ask("Enter the target directory to save the parsed files: ")

  # Call the function to parse the log file
  parse_log_file(log_file_path, target_directory)