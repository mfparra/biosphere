from Src.BioDataManagement.CrossCutting.DTOs.BiologicalMeasureTypeDto import BiologicalMeasureTypeDto


class MicroRnaExpressionLevelDto:
    """description of class"""

    def __init__(self, **kargs):
        """

        :param kargs: 
        """
        self.__biological_measure_type = BiologicalMeasureTypeDto(**kargs)
        self.__symbol = kargs.get('symbol')

    def __hash__(self):
        return hash(self.__symbol)

    def __eq__(self, other):
        return isinstance(other, MicroRnaExpressionLevelDto) and \
               self.__symbol== other.symbol

    @property
    def symbol(self) -> str:
        """description of property"""
        return self.__symbol

    @symbol.setter
    def symbol(self, value: str):
        """

        :param value: 
        :return: 
        """
        self.__symbol = value

    @property
    def control_value(self) -> float:
        """description of property"""
        return self.__biological_measure_type.control_value

    @control_value.setter
    def control_value(self, value: float):
        """

        :param value: 
        :return: 
        """
        self.__biological_measure_type.control_value = value

    @property
    def case_value(self) -> float:
        """description of property"""
        return self.__biological_measure_type.case_value

    @case_value.setter
    def case_value(self, value: float):
        """

        :param value: 
        :return: 
        """
        self.__biological_measure_type.case_value = value