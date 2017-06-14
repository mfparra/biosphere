import unittest
from unittest.mock import Mock, patch
from yaak import inject

from Src.BioDataManagement.CrossCutting.Contracts.MessengerRnaSampleRepositoryBase import \
    MessengerRnaSampleRepositoryBase
from Src.BioDataManagement.CrossCutting.DTOs.GeneExpressionLevelDto import GeneExpressionLevelDto
from Src.BioDataManagement.CrossCutting.DTOs.MessengerRnaSampleDto import MessengerRnaSampleDto
from Src.BioDataManagement.CrossCutting.Filters.FeListMessengerRnaSample import FeListMessengerRnaSample
from Src.BioDataManagement.Managers.MessengerRnaSampleManager import MessengerRnaSampleManager


class MessemgerRnaSampleManagerTests(unittest.TestCase):
    def setUp(self):
        self.__messenger_rna_sample_dto = [MessengerRnaSampleDto(patient_id='TCGA-A7-A0DB',
                                                                 gene_expression_levels=[GeneExpressionLevelDto(id_entrez=1,
                                                                                                                control_value=0.1,
                                                                                                                case_value=12),
                                                                                         GeneExpressionLevelDto(id_entrez=12,
                                                                                                                control_value=0.1,
                                                                                                                case_value=12),
                                                                                         GeneExpressionLevelDto(id_entrez=1,
                                                                                                                control_value=0.1,
                                                                                                                case_value=12),
                                                                                         GeneExpressionLevelDto(id_entrez=14,
                                                                                                                control_value=0.1,
                                                                                                                case_value=12)]),
                                           MessengerRnaSampleDto(patient_id='TCGA-E7-A0DB',
                                                                 gene_expression_levels=[GeneExpressionLevelDto(id_entrez=1,
                                                                                                                control_value=0.1,
                                                                                                                case_value=12),
                                                                                         GeneExpressionLevelDto(id_entrez=12,
                                                                                                                control_value=0.1,
                                                                                                                case_value=12),
                                                                                         GeneExpressionLevelDto(id_entrez=1,
                                                                                                                control_value=0.1,
                                                                                                                case_value=12),
                                                                                         GeneExpressionLevelDto(id_entrez=14,
                                                                                                                control_value=0.1,
                                                                                                                case_value=12)]),
                                           MessengerRnaSampleDto(patient_id='TCGA-A3-A0DB',
                                                                 gene_expression_levels=[GeneExpressionLevelDto(id_entrez=1,
                                                                                                                control_value=0.1,
                                                                                                                case_value=12),
                                                                                         GeneExpressionLevelDto(id_entrez=12,
                                                                                                                control_value=0.1,
                                                                                                                case_value=12),
                                                                                         GeneExpressionLevelDto(id_entrez=1,
                                                                                                                control_value=0.1,
                                                                                                                case_value=12),
                                                                                         GeneExpressionLevelDto(id_entrez=14,
                                                                                                                control_value=0.1,
                                                                                                                case_value=12)]),
                                           MessengerRnaSampleDto(patient_id='TCGA-A7-A0DB',
                                                                 gene_expression_levels=[GeneExpressionLevelDto(id_entrez=1,
                                                                                                                control_value=0.1,
                                                                                                                case_value=12),
                                                                                         GeneExpressionLevelDto(id_entrez=12,
                                                                                                                control_value=0.1,
                                                                                                                case_value=12),
                                                                                         GeneExpressionLevelDto(id_entrez=1,
                                                                                                                control_value=0.1,
                                                                                                                case_value=12),
                                                                                         GeneExpressionLevelDto(id_entrez=14,
                                                                                                                control_value=0.1,
                                                                                                                case_value=12)])]

        self.__repository = Mock(spec=MessengerRnaSampleRepositoryBase)
        self.__fe = FeListMessengerRnaSample()
        self.__fe.result_list = [m.patient_id for m in self.__messenger_rna_sample_dto[:-1]]

        self.__repository.get_many.return_value  = self.__fe
        inject.provide('MessengerRnaSampleRepositoryBase', lambda: self.__repository, scope=inject.Scope.Application)
        self.__manager = MessengerRnaSampleManager(self.__repository)

    def tearDown(self):
        inject.clear()

    def test_get_many(self):
        fe =  self.__manager.get_many(FeListMessengerRnaSample())
        self.assertTrue(len(fe.result_list), 3)

    def test_add_many(self):
        with patch.object(self.__repository, 'add_many') as mock:
            self.__manager.add_many(self.__messenger_rna_sample_dto)
            assert not mock.called

        self.__fe.result_list = ['TCGA-A7-A0DB', 'TCGA-E7-A0DB']
        self.__repository.get_many.return_value = self.__fe

        with patch.object(self.__repository, 'add_many') as mock:
            self.__manager.add_many(self.__messenger_rna_sample_dto)
            mock.assert_called_with([MessengerRnaSampleDto(patient_id='TCGA-A3-A0DB',
                                                           gene_expression_levels=[GeneExpressionLevelDto(id_entrez=1,
                                                                                                          control_value=0.1,
                                                                                                          case_value=12),
                                                                                   GeneExpressionLevelDto(id_entrez=12,
                                                                                                          control_value=0.1,
                                                                                                          case_value=12),
                                                                                   GeneExpressionLevelDto(id_entrez=1,
                                                                                                          control_value=0.1,
                                                                                                          case_value=12),
                                                                                   GeneExpressionLevelDto(id_entrez=14,
                                                                                                          control_value=0.1,
                                                                                                          case_value=12)])])

if __name__ == '__main__':
    unittest.main()
