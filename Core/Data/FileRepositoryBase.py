from abc import ABCMeta

from Core.File.FileUtils import FileUtils


class FileRepositoryBase(metaclass=ABCMeta):
    """
    
    """
    def __init__(self, directory:str):
        """
        
        :param directory: 
        """
        if not FileUtils.is_directory(directory):
            raise NotADirectoryError('The directory not found.')

        self.__directory = directory

    @property
    def _directory(self) -> str:
        """        
        :return: 
        """
        return self.__directory
