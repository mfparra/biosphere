from typing import List, Dict

from Src.BioDataManagement.CrossCutting.DTOs.MessengerRnaSampleDto import MessengerRnaSampleDto
from Src.BioDataManagement.CrossCutting.Filters.FeListMessengerRnaSample import FeListMessengerRnaSample
from Src.Core.Manager.ManagerBase import ManagerBase


class MessengerRnaSampleManager(ManagerBase):
    """description of class"""

    def __init__(self, repository):
        """
        
        :param repository: 
        """
        super().__init__(repository)


    def add_many(self, mrna_samples: List[MessengerRnaSampleDto]):
        """
        
        :param mrna_samples: 
        :return: 
        """
        fe_samples = self._repository.get_many(
            FeListMessengerRnaSample(is_paged=False, patient_id_list=[mrna.patient_id for mrna in mrna_samples]),
            {'patient_id':1})

        new_samples = [m for m in mrna_samples if m.patient_id not in fe_samples.result_list]

        if not new_samples:
            return

        self._repository.add_many(new_samples)

    def get_many(self, fe_mrna: FeListMessengerRnaSample,
                 include_or_exclude_fields: Dict[str, int] = None) -> FeListMessengerRnaSample:
        """
        
        :param fe_gene: 
        :param include_or_exclude_fields: 
        :return: 
        """
        if not fe_mrna.gene_expression_levels_from_patients:
            return self._repository.get_many(fe_mrna, MessengerRnaSampleDto, include_or_exclude_fields)

        fe_mrna = self._repository.get_many(fe_mrna, MessengerRnaSampleDto, include_or_exclude_fields)

        fe_mrna.result_list = [MessengerRnaSampleDto(patient_id=m.patient_id,
                                                     exp_levels=[exp for exp in m.exp_levels if exp.id_entrez in
                                                                    fe_mrna.gene_expression_levels_from_patients[m.patient_id]])
                                                                 for m in fe_mrna.result_list]

        return fe_mrna