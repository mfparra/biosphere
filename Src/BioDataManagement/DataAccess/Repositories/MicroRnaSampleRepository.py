from typing import List, Dict

from Src.BioDataManagement.CrossCutting.Contracts.MicroRnaSampleRepositoryBase import MicroRnaSampleRepositoryBase
from Src.BioDataManagement.CrossCutting.DTOs.MicroRnaSampleDto import MicroRnaSampleDto
from Src.BioDataManagement.CrossCutting.Filters.FeListMicroRnaSample import FeListMicroRnaSample
from Src.BioDataManagement.DataAccess.Entities.MicroRnaSample import MicroRnaSample
from Src.Core.Data.MongoRepositoryActions import MongoRepositoryActions


class MicroRnaSampleRepository(MicroRnaSampleRepositoryBase):
    """description of class"""

    def __init__(self, db):
        """
        
        :param db: 
        """
        super().__init__(db, 'micro_rna_sample')
        self.__mongo_actions = MongoRepositoryActions(self._collection)

    def add_many(self, mirna_samples: List[MicroRnaSampleDto]):
        """
        
        :param mirna_samples: 
        """
        self.__mongo_actions.add_many(mirna_samples, MicroRnaSample)

    def get_many(self, fe_mirna_sample: FeListMicroRnaSample, dto_class = None,
                 include_or_exclude_fields: Dict[str, int] = None) -> FeListMicroRnaSample:
        """
        
        :param fe_mirna_sample: 
        :param dto_class: 
        :param include_or_exclude_fields: 
        :return: 
        """
        query = {} if not fe_mirna_sample.patient_id_list \
            else {'patient_id': {'$in': fe_mirna_sample.patient_id_list}}

        return self.__mongo_actions.get_many(query,
                                             fe_mirna_sample,
                                             MicroRnaSample,
                                             dto_class,
                                             include_or_exclude_fields)
