from typing import Dict, List

from Src.BioDataManagement.CrossCutting.Filters.FeListSampleBase import FeListSampleBase


class FeListDnaMethylationSample(FeListSampleBase):
    """description of class"""

    def __init__(self, **kargs):
        """description of initialize"""

        super().__init__(**kargs)
        self.__dna_methylation_levels_from_patients = kargs.get("dna_methylation_levels_from_patients", {})

    @property
    def dna_methylation_levels_from_patients(self) -> Dict[str, List[int]]:
        """description of property"""
        return dict(self.__dna_methylation_levels_from_patients)