class BiologicalMeasureType:
    """description of class"""

    def __init__(self, **kargs):
        """
        
        :param kargs: 
        """
        self.__control_value = kargs.get('control_value', None)
        self.__case_value = kargs.get('case_value', None)

        if not self.__control_value == 0 and not self.__control_value:
            raise ValueError("The 'control_value' is required.")

        if not self.__case_value == 0 and not self.__case_value:
            raise ValueError("The 'case_value' is required.")


    @property
    def control_value(self) -> float:
        """description of property"""
        return self.__control_value

    @property
    def case_value(self) -> float:
        """description of property"""
        return self.__case_value