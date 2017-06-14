from typing import List

from Src.BioDataFileManagement.CrossCutting.Entities.BiologicalFileSampleBase import BiologicalFileSampleBase
from Src.BioDataFileManagement.CrossCutting.Entities.MicroRnaExpressionLevel import MicroRnaExpressionLevel


class MicroRnaSampleFile(BiologicalFileSampleBase):
    """description of class"""

    def __init__(self, **kargs):
        """

        :param kargs: 
        """
        super().__init__(**kargs)

        self.__micro_rna_expression_levels = kargs.get("micro_rna_expression_levels")

        if not self.__micro_rna_expression_levels:
            raise ValueError("The 'micro_rna_expression_levels' is required.")
        else:
            self.__micro_rna_expression_levels = list(set(self.__micro_rna_expression_levels))

    def __hash__(self):
        return hash(self.patient_id)

    def __eq__(self, other):
        return isinstance(other, MicroRnaSampleFile) and \
               self.patient_id == other.patient_id

    @property
    def micro_rna_expression_levels(self) -> List[MicroRnaExpressionLevel]:
        """description of property"""
        return self.__micro_rna_expression_levels[:]