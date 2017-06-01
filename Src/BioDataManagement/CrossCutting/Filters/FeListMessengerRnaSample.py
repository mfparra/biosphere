from typing import Dict, List

from Src.BioDataManagement.CrossCutting.Filters.FeListSampleBase import FeListSampleBase


class FeListMessengerRnaSample(FeListSampleBase):
    """description of class"""

    def __init__(self, **kargs):
        """description of initialize"""

        super().__init__(**kargs)
        self.__gene_expression_levels_from_patients = kargs.get("gene_expression_levels_from_patients", {})

    @property
    def gene_expression_levels_from_patients(self) -> Dict[str, List[int]]:
        """description of property"""
        return dict(self.__gene_expression_levels_from_patients)