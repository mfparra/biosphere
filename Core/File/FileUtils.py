import os


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
