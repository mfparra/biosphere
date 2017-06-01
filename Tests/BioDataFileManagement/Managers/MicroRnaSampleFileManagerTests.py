import unittest
from unittest.mock import Mock

from Src.BioDataFileManagement.CrossCutting.Contracts.MicroRnaSampleFileRepositoryBase import \
    MicroRnaSampleFileRepositoryBase
from Src.BioDataFileManagement.CrossCutting.Entities.MicroRnaExpressionLevel import MicroRnaExpressionLevel
from Src.BioDataFileManagement.CrossCutting.Entities.MicroRnaSampleFile import MicroRnaSampleFile
from Src.BioDataFileManagement.Managers.MessengerRnaSampleFileManager import MessengerRnaSampleFileManager
from Src.BioDataManagement.CrossCutting.Filters.FeListGeneAnnotation import FeListGeneAnnotation


class MicroRnaSampleFileManagerTests(unittest.TestCase):
    def setUp(self):
        micro_rna_expression_levels = [MicroRnaExpressionLevel(symbol='ABC',
                                                               control_value=1.21,
                                                               case_value=2.3),
                                       MicroRnaExpressionLevel(symbol='ABC',
                                                               control_value=1.2,
                                                               case_value=2.3),
                                       MicroRnaExpressionLevel(symbol='AKS2',
                                                               control_value=0.21,
                                                               case_value=2.3),
                                       MicroRnaExpressionLevel(symbol='AHD1',
                                                               control_value=0.31,
                                                               case_value=2.3),
                                       MicroRnaExpressionLevel(symbol='ABCQ',
                                                               control_value=4.09,
                                                               case_value=4.3)]

        self.__fe = FeListGeneAnnotation()
        self.__fe.result_list = [MicroRnaSampleFile(patient_id='TCGA-A7-A0D9',
                                                    micro_rna_expression_levels=micro_rna_expression_levels),
                                 MicroRnaSampleFile(patient_id='TCGA-A7-A0DC',
                                                    micro_rna_expression_levels=micro_rna_expression_levels),
                                 MicroRnaSampleFile(patient_id='TCGA-AC-A23H',
                                                    micro_rna_expression_levels=micro_rna_expression_levels),
                                 MicroRnaSampleFile(patient_id='TCGA-BH-A0B8',
                                                    micro_rna_expression_levels=micro_rna_expression_levels),
                                 MicroRnaSampleFile(patient_id='TCGA-A7-A0DC',
                                                    micro_rna_expression_levels=micro_rna_expression_levels)]

        self.__repository = Mock(spec=MicroRnaSampleFileRepositoryBase)
        self.__repository.get.return_value = self.__fe

    def test_get(self):
        manager = MessengerRnaSampleFileManager(self.__repository)
        filter = manager.get(FeListGeneAnnotation())

        self.assertTrue(len(filter.result_list) == 4)
        self.assertTrue(len([mirna.micro_rna_expression_levels for mirna in filter.result_list
                             if len(mirna.micro_rna_expression_levels) == 4]) == 4)


if __name__ == '__main__':
    unittest.main()
