# import pytest
# from unittest.mock import patch
# from automation.create_folder import create_folder
# from automation.temp_folder import move_user_documents


# class FolderAndFileOperationsTest(self, unittest.TestCase):
#     @patch('automation.createFolder.os.mkdir')
#     def test_create_folder(self, mock_mkdir):
#         folder_name = "test_folder"
#         create_folder(folder_name)
#         mock_mkdir.assert_called_once_with(folder_name)

# def test_autmoation():
#     assert True

# def test_create_folder(self, mock_mkdir):
#         folder_name = "test_folder"
#         create_folder(folder_name)
#         mock_mkdir.assert_called_once_with(folder_name)

# @patch('automation.deleteUser.shutil.move')
# def test_move_user_documents_folder_and_file_exist(self, mock_move):
#     folder = "test_folder"
#     file = "test_file.txt"
#     move_user_documents(folder, file)
#     mock_move.assert_called_once_with(f'{folder}/{file}', "temp")

import pytest
from unittest.mock import patch, Mock
from rich.prompt import Prompt
from rich.console import Console
from automation.create_folder import make_folder
# from automation.temp_folder import move_user_documents
# from automation.sort_folder import sort_documents
# from automation.parse_file import parse_log_file
# from automation.rename_pattern import name_pattern


def test_automation():
  assert True

def test_create_folder():
  with patch('automation.create_folder.os.mkdir') as mock_mkdir:
    folder_name = "test_folder"
    make_folder(folder_name)
    mock_mkdir.assert_called_once_with(folder_name)

@pytest.mark.skip('testing')
def test_move_user_documents_folder_and_file_exist():
  with patch('automation.deleteUser.shutil.move') as mock_move:
    folder = "test_folder"
    file = "test_file.txt"
    move_user_documents(folder, file)
    mock_move.assert_called_once_with(f'{folder}/{file}', "temp")