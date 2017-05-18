from typing import List

from Src.BioDataFileManagement.CrossCutting.Entities.BiologicalFileSampleBase import BiologicalFileSampleBase
from Src.BioDataFileManagement.CrossCutting.Entities.GeneExpressionLevel import GeneExpressionLevel


class MessengerRnaSampleFile(BiologicalFileSampleBase):
    """description of class"""

    def __init__(self, **kargs):
        """

        :param kargs: 
        """
        super().__init__(**kargs)

        self.__gene_expression_levels = kargs.get("gene_expression_levels")

        if not self.__gene_expression_levels:
            raise ValueError("The 'gene_expression_levels' is required.")
        else:
            self.__gene_expression_levels = list(set(self.__gene_expression_levels))

    def __hash__(self):
        return hash(self.patient_id)

    def __eq__(self, other):
        return isinstance(other, MessengerRnaSampleFile) and \
               self.patient_id == other.patient_id

    @property
    def gene_expression_levels(self) -> List[GeneExpressionLevel]:
        """description of property"""
        return self.__gene_expression_levels[:]