from typing import List

from Src.BioDataManagement.CrossCutting.DTOs.BiologicalSampleBaseDto import BiologicalSampleBaseDto
from Src.BioDataManagement.CrossCutting.DTOs.MicroRnaExpressionLevelDto import MicroRnaExpressionLevelDto


class MicroRnaSampleDto(BiologicalSampleBaseDto):
    """description of class"""

    def __init__(self, **kargs):
        """

        :param kargs: 
        """
        super().__init__(**kargs)

        self.__mirna_expression_levels = kargs.get("mirna_expression_levels")

        if self.__mirna_expression_levels:
            self.__mirna_expression_levels = list(set(self.__mirna_expression_levels))

    def __hash__(self):
        return hash(self.patient_id)

    def __eq__(self, other):
        return isinstance(other, MicroRnaSampleDto) and \
               self.patient_id == other.patient_id

    @property
    def mirna_expression_levels(self) -> List[MicroRnaExpressionLevelDto]:
        """description of property"""
        return self.__mirna_expression_levels[:]

    @mirna_expression_levels.setter
    def mirna_expression_levels(self, value: List[MicroRnaExpressionLevelDto]):
        """

        :param value: 
        :return: 
        """
        self.__mirna_expression_levels = value
