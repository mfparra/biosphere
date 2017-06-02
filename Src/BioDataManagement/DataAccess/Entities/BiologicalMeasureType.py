from Src.Core.Entity.EntityBase import EntityBase


class BiologicalMeasureType(EntityBase):
    """description of class"""

    def __init__(self, **kargs):
        """
        
        :param kargs: 
        """
        self.__control = kargs.get('control', None)
        self.__case = kargs.get('case', None)

    @property
    def control(self) -> float:
        """description of property"""
        return self.__control

    @control.setter
    def control(self, value: float):
        """

        :param value: 
        :return: 
        """
        self.__control = value

    @property
    def case(self) -> float:
        """description of property"""
        return self.__case

    @case.setter
    def case(self, value: float):
        """

        :param value: 
        :return: 
        """
        self.__case = value

    def validate(self):
        if not self.__case:
            raise ValueError('Case is required.')

        if not self.__control:
            raise ValueError('Control is required.')

    def as_dict(self):
        return {'case': self.__case,
                'control': self.__control}