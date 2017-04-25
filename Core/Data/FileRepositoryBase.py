from abc import ABCMeta


class FileRepositoryBase(metaclass=ABCMeta):
    """
    
    """

    @property
    def _root_path(self) -> str:
        """        
        :return: 
        """
        return self.__root_path
