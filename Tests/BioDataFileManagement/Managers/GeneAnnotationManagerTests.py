import unittest
from unittest.mock import Mock
from yaak import inject

from Src.BioDataFileManagement.CrossCutting.Contracts.GeneAnnotationFileRepositoryBase import \
    GeneAnnotationFileRepositoryBase
from Src.BioDataFileManagement.CrossCutting.Entities.GeneAnnotationFile import GeneAnnotationFile
from Src.BioDataFileManagement.CrossCutting.Filters.FeSingleGeneAnnotationFile import FeSingleGeneAnnotationFile
from Src.BioDataFileManagement.Managers.GeneAnnotionFileManager import GeneAnnotationFileManager


class GeneAnnotationManagerTests(unittest.TestCase):
    def setUp(self):
        self.__fe = FeSingleGeneAnnotationFile(file='gene_annotation.txt')
        self.__fe.result = [GeneAnnotationFile(id_entrez=12, symbol='A2MP1',
                                               synonyms_genes=['A2MD', 'CPAMD5', 'FWP007', 'S863-7']),
                            GeneAnnotationFile(id_entrez=121, symbol='ACACB',
                                               synonyms_genes=['HEL70']),
                            GeneAnnotationFile(id_entrez=1, symbol='RPS10-NUDT3',
                                               synonyms_genes=['-']),
                            GeneAnnotationFile(id_entrez=89, symbol='AANAT',
                                               synonyms_genes=['-'])]

        self.__repository = Mock(spec=GeneAnnotationFileRepositoryBase)
        self.__repository.get.return_value = self.__fe

        inject.provide('GeneAnnotationFileRepositoryBase', lambda: self.__repository, scope=inject.Scope.Application)

    def tearDown(self):
        inject.clear()

    def test_get(self):
        filter = FeSingleGeneAnnotationFile(file='gene_annotation.txt')
        manager = GeneAnnotationFileManager()

        filter_result = manager.get(filter)

        self.assertTrue(len(filter_result.result) == 4)
        self.assertTrue(len([ga.synonyms_genes for ga in filter_result.result if ga.synonyms_genes]) == 2)


if __name__ == '__main__':
    unittest.main()
