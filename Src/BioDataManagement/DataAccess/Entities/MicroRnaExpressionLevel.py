from Src.BioDataManagement.DataAccess.Entities.BiologicalMeasureType import BiologicalMeasureType
from Src.Core.Entity.EntityBase import EntityBase


class MicroRnaExpressionLevel(EntityBase):
    """description of class"""

    def __init__(self, **kargs):
        """

        :param kargs: 
        """
        self.__biological_measure_type = BiologicalMeasureType(**kargs)
        self.__symbol = kargs.get('symbol')

    def __hash__(self):
        return hash(self.__symbol)

    def __eq__(self, other):
        return isinstance(other, MicroRnaExpressionLevel) and \
               self.__symbol == other.symbol

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
    def control(self) -> float:
        """description of property"""
        return self.__biological_measure_type.control

    @control.setter
    def control(self, value: float):
        """

        :param value: 
        :return: 
        """
        self.__biological_measure_type.control = value

    @property
    def case(self) -> float:
        """description of property"""
        return self.__biological_measure_type.case

    @case.setter
    def case(self, value: float):
        """

        :param value: 
        :return: 
        """
        self.__biological_measure_type.case = value

    def validate(self):
        super().validate()

        if not self.__symbol:
            raise ValueError('symbol is required.')

        if not self.case:
            raise ValueError('case is required.')

        if not self.control:
            raise ValueError('control is required.')

    def as_dict(self):
        return {'symbol': self.__symbol,
                'case': self.case,
                'control': self.control}