import glob
import re
import os
from typing import List
from os import path


class FileUtils:
    """
    
    """

    @staticmethod
    def is_directory(directory: str):
        """
        
        :param directory: 
        :return: 
        """
        return os.path.isdir(directory)

    @staticmethod
    def is_file(file: str):
        """
        
        :param file: 
        :return: 
        """
        return os.path.isfile(file)

    @staticmethod
    def read(file_fullname: str) -> str:
        """
        
        :param file_fullname: 
        :return: 
        """
        content = ''

        with open(file_fullname, 'r') as file:
            content = file.read()

        return content

    @staticmethod
    def read_all(directory:str, pattern: str = None, recursive: bool = False):
        """
        
        :param directory: 
        :param pattern: 
        :param recursive: 
        :return: 
        """
        files = FileUtils.get(directory, pattern, recursive)
        return dict([(FileUtils.get_file_name(file), FileUtils.read(path.join(directory, file))) for file in files])

    @staticmethod
    def read_with_pagginate(directory: str, page_size: int, current_page: int, page_count: int, pattern: str = None,
                            recursive: bool = False):
        """

        :param directory:         
        :param page_size: 
        :param current_page: 
        :param page_count: 
        :param pattern: 
        :param recursive: 
        :return: 
        """
        files = FileUtils.get(directory, pattern, recursive)

        start_row = page_size * current_page
        result_count = len(files)

        file_list = files[start_row: (start_row + page_size)]
        div_result = divmod(result_count, page_size)
        page_count = div_result[0]

        if div_result[1] > 0:
            page_count += 1
        else:
            page_count = 1

        current_page += 1
        result_list = dict([(FileUtils.get_file_name(file), FileUtils.read(path.join(directory, file))) for file in
                            file_list])

        return current_page, page_count, result_list

    @staticmethod
    def get_file_name(file: str) -> str:
        """
        
        :param file: 
        :return: 
        """
        return path.splitext(file)[0]

    @staticmethod
    def get(directory:str, pattern:str=None, recursive:bool=False)->List[str]:
        """
        
        :param directory: 
        :param pattern: 
        :param recursive: 
        :return: 
        """
        directories = filter(path.isdir, os.listdir(directory)) if recursive\
                      else [directory]

        if not pattern:
            return [filename for d in directories for filename in os.listdir(d)]

        re_filename = re.compile(pattern)
        return [filename for d in directories for filename in os.listdir(d) if re_filename.search(filename)]