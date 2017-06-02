from typing import List, Dict

from Src.BioDataManagement.CrossCutting.Contracts.DnaMethylationSampleRepositoryBase import \
    DnaMethylationSampleRepositoryBase
from Src.BioDataManagement.CrossCutting.DTOs.DnaMethylationSampleDto import DnaMethylationSampleDto
from Src.BioDataManagement.CrossCutting.Filters import FeListDnaMethylationSample
from Src.BioDataManagement.DataAccess.Entities.DnaMethylationSample import DnaMethylationSample
from Src.Core.Data.MongoRepositoryActions import MongoRepositoryActions


class DnaMethylationSampleRepository(DnaMethylationSampleRepositoryBase):
    """description of class"""

    def __init__(self, db):
        """
        
        :param db: 
        """
        super().__init__(db, 'dna_methylation_sample')
        self.__mongo_actions = MongoRepositoryActions(self._collection)

    def add_many(self, dna_methylation_samples: List[DnaMethylationSampleDto]):
        """
        
        :param dna_methylation_samples: 
        """
        self.__mongo_actions.add_many(dna_methylation_samples, DnaMethylationSample)

    def get_many(self, fe_dna_methylation_sample: FeListDnaMethylationSample, dto_class = None,
                 include_or_exclude_fields: Dict[str, int] = None) -> FeListDnaMethylationSample:
        """
        
        :param fe_dna_methylation_sample: 
        :param dto_class: 
        :param include_or_exclude_fields: 
        :return: 
        """
        query = {} if not fe_dna_methylation_sample.patient_id_list \
            else {'patient_id': {'$in': fe_dna_methylation_sample.patient_id_list}}

        return self.__mongo_actions.get_many(query,
                                             fe_dna_methylation_sample,
                                             DnaMethylationSample,
                                             dto_class,
                                             include_or_exclude_fields)
