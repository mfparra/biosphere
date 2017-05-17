from typing import List

from Src.BioDataFileManagement.CrossCutting.Entities.DnaMethylationLevel import DnaMethylationLevel
from Src.BioDataFileManagement.CrossCutting.Entities.BiologicalFileSampleBase import BiologicalFileSampleBase


class DnaMethylationSampleFile(BiologicalFileSampleBase):
    """description of class"""

    def __init__(self, **kargs):
        """

        :param kargs: 
        """
        super().__init__(**kargs)

        self.__dna_methylation_levels = kargs.get("dna_methylation_levels")

        if not self.__dna_methylation_levels:
            raise ValueError("The 'dna_methylation_levels' is required.")
        else:
            self.__dna_methylation_levels = list(set(self.__dna_methylation_levels))

    def __hash__(self):
        return hash(self.patient_id)

    def __eq__(self, other):
        return isinstance(other, DnaMethylationSampleFile) and \
               self.patient_id == other.patient_id

    @property
    def dna_methylation_levels(self) -> List[DnaMethylationLevel]:
        """description of property"""
        return self.__dna_methylation_levels[:]