from abc import ABCMeta


class MongoRepositoryBase(metaclass = ABCMeta):
    """description of class"""

    def __init__(self, db, collection_name:str):
        """
        
        :param db: 
        :param collection_name: 
        """
        if type(db) == type(None):
            raise ValueError("The 'db' is required.")

        if collection_name:
            raise ValueError('The collection_name is required.')

        self.__collection = db[collection_name]

    @property
    def _collection(self):
        """description of property"""
        return self.__collection