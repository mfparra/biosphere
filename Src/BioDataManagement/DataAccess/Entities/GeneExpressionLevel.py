from Src.BioDataManagement.DataAccess.Entities.BiologicalMeasureType import BiologicalMeasureType
from Src.Core.Entity.EntityBase import EntityBase


class GeneExpressionLevel(EntityBase):
    """description of class"""

    def __init__(self, **kargs):
        """

        :param kargs: 
        """
        self.__biological_measure_type = BiologicalMeasureType(**kargs)
        self.__id_entrez = kargs.get('id_entrez')

    def __hash__(self):
        return hash(self.__id_entrez)

    def __eq__(self, other):
        return isinstance(other, GeneExpressionLevel) and \
               self.__id_entrez == other.id_entrez

    @property
    def id_entrez(self) -> int:
        """description of property"""
        return self.__id_entrez

    @id_entrez.setter
    def id_entrez(self, value: int):
        """

        :param value: 
        :return: 
        """
        self.__id_entrez = value

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
        self.__biological_measure_type.case_value = value

    def validate(self):
        super().validate()

        if not self.__id_entrez:
            raise ValueError('id_entrez is required.')

        if not self.case:
            raise ValueError('case is required.')

        if not self.control:
            raise ValueError('control is required.')

    def as_dict(self):
        return {'id_entrez': self.__id_entrez,
                'case': self.case,
                'control': self.control}