from typing import List, Dict

from Src.BioDataManagement.CrossCutting.Contracts.MessengerRnaSampleRepositoryBase import \
    MessengerRnaSampleRepositoryBase
from Src.BioDataManagement.CrossCutting.DTOs.MessengerRnaSampleDto import MessengerRnaSampleDto
from Src.BioDataManagement.CrossCutting.Filters.FeListMessengerRnaSample import FeListMessengerRnaSample
from Src.BioDataManagement.DataAccess.Entities.MessengerRnaSample import MessengerRnaSample
from Src.Core.Data.MongoRepositoryActions import MongoRepositoryActions


class MessengerRnaSampleRepository(MessengerRnaSampleRepositoryBase):
    """description of class"""

    def __init__(self, db):
        """
        
        :param db: 
        """
        super().__init__(db, 'micro_rna_sample')
        self.__mongo_actions = MongoRepositoryActions(self._collection)

    def add_many(self, mrna_samples: List[MessengerRnaSampleDto]):
        """
        
        :param mrna_samples: 
        """
        self.__mongo_actions.add_many(mrna_samples, MessengerRnaSample)

    def get_many(self, fe_mrna: FeListMessengerRnaSample, dto_class = None,
                 include_or_exclude_fields: Dict[str, int] = None) -> FeListMessengerRnaSample:
        """
        
        :param fe_mrna: 
        :param dto_class: 
        :param include_or_exclude_fields: 
        :return: 
        """
        query = {} if not fe_mrna.patient_id_list \
            else {'patient_id': {'$in': fe_mrna.patient_id_list}}

        return self.__mongo_actions.get_many(query, fe_mrna, MessengerRnaSample, dto_class, include_or_exclude_fields)
