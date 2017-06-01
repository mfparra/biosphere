from abc import ABCMeta

from Src.Core.Entity.EntityBase import EntityBase


class BiologicalSampleBase(EntityBase, metaclass=ABCMeta):
    """description of class"""

    def __init__(self, **kargs):
        """
        
        :param kargs: 
        """
        self.__patient_id = kargs.get("patient_id")

    @property
    def patient_id(self) -> str:
        """description of property"""
        return self.__patient_id

    @patient_id.setter
    def patient_id(self, value: str):
        """

        :param value: 
        :return: 
        """
        self.__patient_id = value

    def validate(self):
        if not self.__patient_id:
            raise ValueError('patient_id is required.')

    def as_dict(self):
        return {'patient_id': self.__patient_id}