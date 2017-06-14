import unittest
from unittest.mock import Mock, patch
from yaak import inject

from Src.BioDataManagement.CrossCutting.Contracts.MicroRnaSampleRepositoryBase import \
    MicroRnaSampleRepositoryBase
from Src.BioDataManagement.CrossCutting.DTOs.MicroRnaExpressionLevelDto import MicroRnaExpressionLevelDto
from Src.BioDataManagement.CrossCutting.DTOs.MicroRnaSampleDto import MicroRnaSampleDto
from Src.BioDataManagement.CrossCutting.Filters.FeListMicroRnaSample import FeListMicroRnaSample
from Src.BioDataManagement.Managers.MicroRnaSampleManager import MicroRnaSampleManager


class MessemgerRnaSampleManagerTests(unittest.TestCase):
    def setUp(self):
        self.__mirna_sample_dto = [MicroRnaSampleDto(patient_id='TCGA-A7-A0DB',
                                                     mirna_expression_levels=[MicroRnaExpressionLevelDto(symbol='hsa-mir-392',
                                                                                                         control_value=0.1,
                                                                                                         case_value=12),
                                                                              MicroRnaExpressionLevelDto(symbol='hsa-mir-32',
                                                                                                         control_value=0.1,
                                                                                                         case_value=12),
                                                                              MicroRnaExpressionLevelDto(symbol='hsa-mir-392',
                                                                                                         control_value=0.1,
                                                                                                         case_value=12),
                                                                              MicroRnaExpressionLevelDto(symbol='hsa-mir-92',
                                                                                                         control_value=0.1,
                                                                                                         case_value=12)]),
                                   MicroRnaSampleDto(patient_id='TCGA-E7-A0DB',
                                                     mirna_expression_levels=[MicroRnaExpressionLevelDto(symbol='hsa-mir-392',
                                                                                                         control_value=0.1,
                                                                                                         case_value=12),
                                                                              MicroRnaExpressionLevelDto(symbol='hsa-mir-192',
                                                                                                         control_value=0.1,
                                                                                                         case_value=12),
                                                                              MicroRnaExpressionLevelDto(symbol='hsa-mir-392',
                                                                                                         control_value=0.1,
                                                                                                         case_value=12),
                                                                              MicroRnaExpressionLevelDto(symbol='hsa-mir-92',
                                                                                                         control_value=0.1,
                                                                                                         case_value=12)]),
                                   MicroRnaSampleDto(patient_id='TCGA-A3-A0DB',
                                                     mirna_expression_levels=[MicroRnaExpressionLevelDto(symbol='hsa-mir-392',
                                                                                                         control_value=0.1,
                                                                                                         case_value=12),
                                                                              MicroRnaExpressionLevelDto(symbol='hsa-mir-92',
                                                                                                         control_value=0.1,
                                                                                                         case_value=12),
                                                                              MicroRnaExpressionLevelDto(symbol='hsa-mir-392',
                                                                                                         control_value=0.1,
                                                                                                         case_value=12),
                                                                              MicroRnaExpressionLevelDto(symbol='hsa-mir-192',
                                                                                                         control_value=0.1,
                                                                                                         case_value=12)]),
                                   MicroRnaSampleDto(patient_id='TCGA-A7-A0DB',
                                                     mirna_expression_levels=[MicroRnaExpressionLevelDto(symbol='hsa-mir-392',
                                                                                                         control_value=0.1,
                                                                                                         case_value=12),
                                                                              MicroRnaExpressionLevelDto(symbol='hsa-mir-92',
                                                                                                        control_value=0.1,
                                                                                                        case_value=12),
                                                                              MicroRnaExpressionLevelDto(symbol='hsa-mir-392',
                                                                                                        control_value=0.1,
                                                                                                        case_value=12),
                                                                              MicroRnaExpressionLevelDto(symbol='hsa-mir-39',
                                                                                                        control_value=0.1,
                                                                                                        case_value=12)])]

        self.__repository = Mock(spec=MicroRnaSampleRepositoryBase)
        self.__fe = FeListMicroRnaSample()
        self.__fe.result_list = [m.patient_id for m in self.__mirna_sample_dto[:-1]]

        self.__repository.get_many.return_value  = self.__fe
        inject.provide('MicroRnaSampleRepositoryBase', lambda: self.__repository, scope=inject.Scope.Application)
        self.__manager = MicroRnaSampleManager(self.__repository)

    def tearDown(self):
        inject.clear()

    def test_get_many(self):
        fe =  self.__manager.get_many(FeListMicroRnaSample())
        self.assertTrue(len(fe.result_list), 3)

    def test_add_many(self):
        with patch.object(self.__repository, 'add_many') as mock:
            self.__manager.add_many(self.__mirna_sample_dto)
            assert not mock.called

        self.__fe.result_list = ['TCGA-A7-A0DB', 'TCGA-E7-A0DB']
        self.__repository.get_many.return_value = self.__fe

        with patch.object(self.__repository, 'add_many') as mock:
            self.__manager.add_many(self.__mirna_sample_dto)
            mock.assert_called_with([MicroRnaSampleDto(patient_id='TCGA-A3-A0DB',
                                                       mirna_expression_levels=[MicroRnaExpressionLevelDto(symbol='hsa-mir-392',
                                                                                                           control_value=0.1,
                                                                                                           case_value=12),
                                                                                MicroRnaExpressionLevelDto(symbol='hsa-mir-92',
                                                                                                           control_value=0.1,
                                                                                                           case_value=12),
                                                                                MicroRnaExpressionLevelDto(symbol='hsa-mir-392',
                                                                                                           control_value=0.1,
                                                                                                           case_value=12),
                                                                                MicroRnaExpressionLevelDto(symbol='hsa-mir-192',
                                                                                                           control_value=0.1,
                                                                                                           case_value=12)])])

if __name__ == '__main__':
    unittest.main()
