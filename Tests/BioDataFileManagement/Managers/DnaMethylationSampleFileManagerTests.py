import unittest
from unittest.mock import Mock

from Src.BioDataFileManagement.CrossCutting.Contracts.DnaMethylationSampleFileRepositoryBase import \
    DnaMethylationSampleFileRepositoryBase
from Src.BioDataFileManagement.CrossCutting.Entities.DnaMethylationLevel import DnaMethylationLevel
from Src.BioDataFileManagement.CrossCutting.Entities.DnaMethylationSampleFile import DnaMethylationSampleFile
from Src.BioDataFileManagement.CrossCutting.Filters.FeListDnaMethylationSampleFile import FeListDnaMethylationSampleFile
from Src.BioDataFileManagement.Managers.DnaMethylationSampleFileManager import DnaMethylationSampleFileManager


class DnaMethylationSampleFileManagerTests(unittest.TestCase):
    def setUp(self):
        dna_mthylation_levels = [DnaMethylationLevel(gene_symbol='ABC',
                                                     control_value=1.21,
                                                     case_value=2.3),
                                 DnaMethylationLevel(gene_symbol='ABC',
                                                     control_value=1.2,
                                                     case_value=2.3),
                                 DnaMethylationLevel(gene_symbol='AKS2',
                                                     control_value=0.21,
                                                     case_value=2.3),
                                 DnaMethylationLevel(gene_symbol='AHD1',
                                                     control_value=0.31,
                                                     case_value=2.3),
                                 DnaMethylationLevel(gene_symbol='ABCQ',
                                                     control_value=4.09,
                                                     case_value=4.3)]

        self.__fe = FeListDnaMethylationSampleFile()
        self.__fe.result_list = [DnaMethylationSampleFile(patient_id='TCGA-A7-A0D9',
                                                          dna_methylation_levels=dna_mthylation_levels),
                                 DnaMethylationSampleFile(patient_id='TCGA-A7-A0DC',
                                                          dna_methylation_levels=dna_mthylation_levels),
                                 DnaMethylationSampleFile(patient_id='TCGA-AC-A23H',
                                                          dna_methylation_levels=dna_mthylation_levels),
                                 DnaMethylationSampleFile(patient_id='TCGA-BH-A0B8',
                                                          dna_methylation_levels=dna_mthylation_levels),
                                 DnaMethylationSampleFile(patient_id='TCGA-A7-A0DC',
                                                          dna_methylation_levels=dna_mthylation_levels)]

        self.__repository = Mock(spec=DnaMethylationSampleFileRepositoryBase)
        self.__repository.get.return_value = self.__fe

    def test_get(self):
        filter = FeListDnaMethylationSampleFile()
        manager = DnaMethylationSampleFileManager(self.__repository)

        filter = manager.get(filter)

        self.assertTrue(len(filter.result_list) == 4)
        self.assertTrue(len([dm.dna_methylation_levels for dm in filter.result_list
                             if len(dm.dna_methylation_levels) == 4]) == 4)


if __name__ == '__main__':
    unittest.main()
