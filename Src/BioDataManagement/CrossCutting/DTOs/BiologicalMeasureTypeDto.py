class BiologicalMeasureTypeDto:
    """description of class"""

    def __init__(self, **kargs):
        """
        
        :param kargs: 
        """
        self.__control_value = kargs.get('control_value', None)
        self.__case_value = kargs.get('case_value', None)

    @property
    def control_value(self) -> float:
        """description of property"""
        return self.__control_value

    @control_value.setter
    def control_value(self, value: float):
        """

        :param value: 
        :return: 
        """
        self.__control_value = value

    @property
    def case_value(self) -> float:
        """description of property"""
        return self.__case_value

    @case_value.setter
    def case_value(self, value: float):
        """

        :param value: 
        :return: 
        """
        self.__case_value = value