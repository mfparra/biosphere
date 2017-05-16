from abc import ABCMeta


class BiologicalFileSampleBase(metaclass=ABCMeta):
    """description of class"""

    def __init__(self, **kargs):
        """
        
        :param kargs: 
        """
        self.__patient_id = kargs.get("patient_id")

        if not self.__patient_id:
            raise ValueError("The 'patient_id' is required.")


    @property
    def patient_id(self) -> str:
        """description of property"""
        return self.__patient_id