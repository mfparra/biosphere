from Src.BioDataManagement.CrossCutting.DTOs.BiologicalMeasureTypeDto import BiologicalMeasureTypeDto


class DnaMethylationLevelDto:
    """description of class"""

    def __init__(self, **kargs):
        """

        :param kargs: 
        """
        self.__biological_measure_type = BiologicalMeasureTypeDto(**kargs)
        self.__id_entrez = kargs.get('id_entrez')

    def __hash__(self):
        return hash(self.__id_entrez)

    def __eq__(self, other):
        return isinstance(other, DnaMethylationLevelDto) and \
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