from abc import ABCMeta


class BiologicalSampleBaseDto(metaclass=ABCMeta):
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