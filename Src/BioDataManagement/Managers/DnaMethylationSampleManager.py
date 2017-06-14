from typing import List, Dict

from yaak import inject

from Src.BioDataManagement.CrossCutting.DTOs.DnaMethylationSampleDto import DnaMethylationSampleDto
from Src.BioDataManagement.CrossCutting.Filters.FeListDnaMethylationSample import FeListDnaMethylationSample
from Src.Core.Manager.ManagerBase import ManagerBase


class DnaMethylationSampleManager(ManagerBase):
    """description of class"""

    @inject.Param(repository='DnaMethylationSampleRepositoryBase')
    def __init__(self, repository):
        """
        
        :param repository: 
        """
        super().__init__(repository)


    def add_many(self, dna_methylation_samples: List[DnaMethylationSampleDto]):
        """
        
        :param dna_methylation_samples: 
        :return: 
        """
        fe_samples = self._repository.get_many(
            FeListDnaMethylationSample(is_paged=False, patient_id_list=[mrna.patient_id for mrna in dna_methylation_samples]),
            {'patient_id':1})

        new_samples = [m for m in dna_methylation_samples if m.patient_id not in fe_samples.result_list]

        if not new_samples:
            return

        self._repository.add_many(new_samples)

    def get_many(self, fe_dna_methylation: FeListDnaMethylationSample,
                 include_or_exclude_fields: Dict[str, int] = None) -> FeListDnaMethylationSample:
        """
        
        :param fe_dna_methylation: 
        :param include_or_exclude_fields: 
        :return: 
        """
        if not fe_dna_methylation.dna_methylation_levels_from_patients:
            return self._repository.get_many(fe_dna_methylation, DnaMethylationSampleDto, include_or_exclude_fields)

        fe_dna_methylation = self._repository.get_many(fe_dna_methylation, DnaMethylationSampleDto, include_or_exclude_fields)

        fe_dna_methylation.result_list = [DnaMethylationSampleDto(patient_id=d.patient_id,
                                                                  levels=[l for l in d.levels if l.id_entrez in
                                                                          fe_dna_methylation.dna_methylation_levels_from_patients[d.patient_id]])
                                                                          for d in fe_dna_methylation.result_list]

        return fe_dna_methylation