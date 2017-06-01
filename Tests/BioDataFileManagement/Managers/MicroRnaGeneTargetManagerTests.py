import unittest
from unittest.mock import Mock

from Src.BioDataFileManagement.CrossCutting.Contracts.MicroRnaGeneTargetFileRepositoryBase import \
    MicroRnaGeneTargetFileRepositoryBase
from Src.BioDataFileManagement.CrossCutting.Entities.GeneAnnotationFile import GeneAnnotationFile
from Src.BioDataFileManagement.CrossCutting.Entities.MicroRnaGeneTargetFile import MicroRnaGeneTargetFile
from Src.BioDataFileManagement.CrossCutting.Filters.FeSingleMicroRnaGeneTargetFile import FeSingleMicroRnaGeneTargetFile
from Src.BioDataFileManagement.Managers.MicroRnaGeneTargetFileManager import MicroRnaGeneTargetFileManager


class MicroRnaGeneTargetManagerTests(unittest.TestCase):
    def setUp(self):
        gene_anotations = [GeneAnnotationFile(id_entrez=12, symbol='A2MP1',
                                              synonyms_genes=['A2MD', 'CPAMD5', 'FWP007', 'S863-7']),
                           GeneAnnotationFile(id_entrez=121, symbol='ACACB',
                                              synonyms_genes=['HEL70']),
                           GeneAnnotationFile(id_entrez=1, symbol='RPS10-NUDT3',
                                              synonyms_genes=['-']),
                           GeneAnnotationFile(id_entrez=89, symbol='AANAT',
                                              synonyms_genes=['-'])]

        targets = [MicroRnaGeneTargetFile(microrna_symbol='hsa-miR-93-5p',
                                          gene_target=gene_anotations[0]),
                   MicroRnaGeneTargetFile(microrna_symbol='hsa-miR-93-5p',
                                          gene_target=gene_anotations[1]),
                   MicroRnaGeneTargetFile(microrna_symbol='hsa-miR-93-5p',
                                          gene_target=gene_anotations[2]),
                   MicroRnaGeneTargetFile(microrna_symbol='hsa-miR-93-5p',
                                          gene_target=gene_anotations[3]),
                   MicroRnaGeneTargetFile(microrna_symbol='hsa-miR-302e',
                                          gene_target=gene_anotations[0]),
                   MicroRnaGeneTargetFile(microrna_symbol='hsa-miR-302e',
                                          gene_target=gene_anotations[0]),
                   MicroRnaGeneTargetFile(microrna_symbol='hsa-miR-1277-5p',
                                          gene_target=gene_anotations[0]),
                   MicroRnaGeneTargetFile(microrna_symbol='hsa-miR-1277-5p',
                                          gene_target=gene_anotations[0])]

        self.__fe = FeSingleMicroRnaGeneTargetFile(file='microrna_gene_target.txt')
        self.__fe.result = targets

        self.__repository = Mock(spec=MicroRnaGeneTargetFileRepositoryBase)
        self.__repository.get.return_value = self.__fe

    def test_get(self):
        filter = FeSingleMicroRnaGeneTargetFile(file='microrna_gene_target.txt')
        manager = MicroRnaGeneTargetFileManager(self.__repository)

        filter_result = manager.get(filter)

        self.assertTrue(len(filter_result.result) == 6)


if __name__ == '__main__':
    unittest.main()
