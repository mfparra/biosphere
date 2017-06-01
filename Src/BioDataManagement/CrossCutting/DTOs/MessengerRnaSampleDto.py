from typing import List

from Src.BioDataManagement.CrossCutting.DTOs.BiologicalSampleBaseDto import BiologicalSampleBaseDto
from Src.BioDataManagement.CrossCutting.DTOs.GeneExpressionLevelDto import GeneExpressionLevelDto


class MessengerRnaSampleDto(BiologicalSampleBaseDto):
    """description of class"""

    def __init__(self, **kargs):
        """

        :param kargs: 
        """
        super().__init__(**kargs)

        self.__gene_expression_levels = kargs.get("gene_expression_levels")
        self.__gene_expression_levels = list(set(self.__gene_expression_levels))

    def __hash__(self):
        return hash(self.patient_id)

    def __eq__(self, other):
        return isinstance(other, MessengerRnaSampleDto) and \
               self.patient_id == other.patient_id

    @property
    def gene_expression_levels(self) -> List[GeneExpressionLevelDto]:
        """description of property"""
        return self.__gene_expression_levels[:]

    @gene_expression_levels.setter
    def gene_expression_levels(self, value: List[GeneExpressionLevelDto]):
        """

        :param value: 
        :return: 
        """
        self.__gene_expression_levels = value
