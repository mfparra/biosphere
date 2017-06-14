import unittest
from unittest.mock import Mock
from yaak import inject

from Src.BioDataFileManagement.CrossCutting.Contracts.MessengerRnaSampleFileRepositoryBase import \
    MessengerRnaSampleFileRepositoryBase
from Src.BioDataFileManagement.CrossCutting.Entities.GeneExpressionLevel import GeneExpressionLevel
from Src.BioDataFileManagement.CrossCutting.Entities.MessengerRnaSampleFile import MessengerRnaSampleFile
from Src.BioDataFileManagement.CrossCutting.Filters.FeListMessengerRnaSampleFile import FeListMessengerRnaSampleFile
from Src.BioDataFileManagement.Managers.MessengerRnaSampleFileManager import MessengerRnaSampleFileManager


class MessengerRnaSampleFileManagerTests(unittest.TestCase):
    def setUp(self):
        gene_expression_levels = [GeneExpressionLevel(gene_symbol='ABC',
                                                      control_value=1.21,
                                                      case_value=2.3),
                                  GeneExpressionLevel(gene_symbol='ABC',
                                                      control_value=1.2,
                                                      case_value=2.3),
                                  GeneExpressionLevel(gene_symbol='AKS2',
                                                      control_value=0.21,
                                                      case_value=2.3),
                                  GeneExpressionLevel(gene_symbol='AHD1',
                                                      control_value=0.31,
                                                      case_value=2.3),
                                  GeneExpressionLevel(gene_symbol='ABCQ',
                                                      control_value=4.09,
                                                      case_value=4.3)]

        self.__fe = FeListMessengerRnaSampleFile()
        self.__fe.result_list = [MessengerRnaSampleFile(patient_id='TCGA-A7-A0D9',
                                                        gene_expression_levels=gene_expression_levels),
                                 MessengerRnaSampleFile(patient_id='TCGA-A7-A0DC',
                                                        gene_expression_levels=gene_expression_levels),
                                 MessengerRnaSampleFile(patient_id='TCGA-AC-A23H',
                                                        gene_expression_levels=gene_expression_levels),
                                 MessengerRnaSampleFile(patient_id='TCGA-BH-A0B8',
                                                        gene_expression_levels=gene_expression_levels),
                                 MessengerRnaSampleFile(patient_id='TCGA-A7-A0DC',
                                                        gene_expression_levels=gene_expression_levels)]

        self.__repository = Mock(spec=MessengerRnaSampleFileRepositoryBase)
        self.__repository.get.return_value = self.__fe

        inject.provide('MessengerRnaSampleFileRepositoryBase', lambda: self.__repository, scope=inject.Scope.Application)

    def tearDown(self):
        inject.clear()

    def test_get(self):
        filter = FeListMessengerRnaSampleFile()
        manager = MessengerRnaSampleFileManager(self.__repository)

        filter = manager.get(filter)

        self.assertTrue(len(filter.result_list) == 4)
        self.assertTrue(len([mrna.gene_expression_levels for mrna in filter.result_list
                             if len(mrna.gene_expression_levels) == 4]) == 4)


if __name__ == '__main__':
    unittest.main()
