from typing import Dict, List

from Src.BioDataManagement.CrossCutting.Filters.FeListSampleBase import FeListSampleBase


class FeListMicroRnaSample(FeListSampleBase):
    """description of class"""

    def __init__(self, **kargs):
        """description of initialize"""

        super().__init__(**kargs)
        self.__mirna_expression_levels_from_patients = kargs.get("mirna_expression_levels_from_patients", {})

    @property
    def mirna_expression_levels_from_patients(self) -> Dict[str, List[str]]:
        """description of property"""
        return dict(self.__mirna_expression_levels_from_patients)