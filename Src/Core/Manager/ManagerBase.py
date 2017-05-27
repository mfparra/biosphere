from abc import ABCMeta


class ManagerBase(metaclass = ABCMeta):
    """
    """

    def __init__(self, repository):
        """
        
        :param repository: 
        """
        if not repository:
            raise ValueError("The 'repository' is required.")

        self.__repository = repository

    @property
    def _repository(self):
        """description of property"""
        return self.__repository