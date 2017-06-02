from typing import List

from Src.BioDataManagement.CrossCutting.DTOs.BiologicalSampleBaseDto import BiologicalSampleBaseDto
from Src.BioDataManagement.CrossCutting.DTOs.DnaMethylationLevelDto import DnaMethylationLevelDto


class DnaMethylationSampleDto(BiologicalSampleBaseDto):
    """description of class"""

    def __init__(self, **kargs):
        """

        :param kargs: 
        """
        super().__init__(**kargs)

        self.__dna_methylation_levels = kargs.get("dna_methylation_levels")

        if self.__dna_methylation_levels:
            self.__dna_methylation_levels = list(set(self.__dna_methylation_levels))

    def __hash__(self):
        return hash(self.patient_id)

    def __eq__(self, other):
        return isinstance(other, DnaMethylationSampleDto) and \
               self.patient_id == other.patient_id

    @property
    def dna_methylation_levels(self) -> List[DnaMethylationLevelDto]:
        """description of property"""
        return self.__dna_methylation_levels[:]

    @dna_methylation_levels.setter
    def dna_methylation_levels(self, value: List[DnaMethylationLevelDto]):
        """

        :param value: 
        :return: 
        """
        self.__dna_methylation_levels = value
