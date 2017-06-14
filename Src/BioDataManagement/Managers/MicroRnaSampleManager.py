from typing import List, Dict

from yaak import inject

from Src.BioDataManagement.CrossCutting.DTOs.MicroRnaSampleDto import MicroRnaSampleDto
from Src.BioDataManagement.CrossCutting.Filters.FeListMicroRnaSample import FeListMicroRnaSample
from Src.Core.Manager.ManagerBase import ManagerBase


class MicroRnaSampleManager(ManagerBase):
    """description of class"""

    @inject.Param(repository='MicroRnaSampleRepositoryBase')
    def __init__(self, repository):
        """
        
        :param repository: 
        """
        super().__init__(repository)


    def add_many(self, mirna_samples: List[MicroRnaSampleDto]):
        """
        
        :param mirna_samples: 
        :return: 
        """
        fe_samples = self._repository.get_many(
            FeListMicroRnaSample(is_paged=False, patient_id_list=[mirna.patient_id for mirna in mirna_samples]),
            {'patient_id':1})

        new_samples = [m for m in mirna_samples if m.patient_id not in fe_samples.result_list]

        if not new_samples:
            return

        self._repository.add_many(new_samples)

    def get_many(self, fe_mirna: FeListMicroRnaSample,
                 include_or_exclude_fields: Dict[str, int] = None) -> FeListMicroRnaSample:
        """
        
        :param fe_mirna: 
        :param include_or_exclude_fields: 
        :return: 
        """
        if not fe_mirna.mirna_expression_levels_from_patients:
            return self._repository.get_many(fe_mirna, MicroRnaSampleDto, include_or_exclude_fields)

        fe_dna_methylation = self._repository.get_many(fe_mirna, MicroRnaSampleDto, include_or_exclude_fields)

        fe_dna_methylation.result_list = [MicroRnaSampleDto(patient_id=m.patient_id,
                                                            mirna_expression_levels=[e for e in m.mirna_expression_levels if e.symbol in
                                                                          fe_mirna.mirna_expression_levels_from_patients[m.patient_id]])
                                                                          for m in fe_dna_methylation.result_list]

        return fe_dna_methylation