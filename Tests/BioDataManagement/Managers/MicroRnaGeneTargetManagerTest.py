import unittest
from unittest.mock import Mock, patch
from yaak import inject

from Src.BioDataManagement.CrossCutting.Contracts.MicroRnaGeneTargetRepositoryBase import \
    MicroRnaGeneTargetRepositoryBase
from Src.BioDataManagement.CrossCutting.DTOs.MicroRnaGeneTargetDto import MicroRnaGeneTargetDto
from Src.BioDataManagement.CrossCutting.Filters.FeListMicroRnaGeneTarget import FeListMicroRnaGeneTarget
from Src.BioDataManagement.Managers.MicroRnaGeneTargetManager import MicroRnaGeneTargetManager


class MicroRnaGeneTargetManagerTests(unittest.TestCase):
    def setUp(self):
        self.__micro_rna_gene_target_dtos = [MicroRnaGeneTargetDto(micro_rna_symbol='hsa-mir-392',
                                                                   id_entrez_genes=[1, 2, 3, 4, 5]),
                                             MicroRnaGeneTargetDto(micro_rna_symbol='hsa-mir-32',
                                                                   id_entrez_genes=[1, 2, 3, 4, 5]),
                                             MicroRnaGeneTargetDto(micro_rna_symbol='hsa-mir-3921',
                                                                   id_entrez_genes=[1, 2, 3, 4, 5]),
                                             MicroRnaGeneTargetDto(micro_rna_symbol='hsa-mir-1392',
                                                                   id_entrez_genes=[1, 2, 3, 4, 5]),
                                             MicroRnaGeneTargetDto(micro_rna_symbol='hsa-mir-3992',
                                                                   id_entrez_genes=[1, 2, 3, 4, 5]),
                                             MicroRnaGeneTargetDto(micro_rna_symbol='hsa-mir-392',
                                                                   id_entrez_genes=[1, 2, 3, 4, 5])]

        self.__repository = Mock(spec=MicroRnaGeneTargetRepositoryBase)
        self.__fe = FeListMicroRnaGeneTarget()
        self.__fe.result_list = [t.micro_rna_symbol for t in self.__micro_rna_gene_target_dtos[:-1]]

        self.__repository.get_many.return_value  = self.__fe
        inject.provide('MicroRnaGeneTargetRepositoryBase', lambda: self.__repository, scope=inject.Scope.Application)
        self.__manager = MicroRnaGeneTargetManager(self.__repository)

    def tearDown(self):
        inject.clear()

    def test_get_many(self):
        fe =  self.__manager.get_many(FeListMicroRnaGeneTarget())
        self.assertTrue(len(fe.result_list), 5)

    def test_add_many(self):
        with patch.object(self.__repository, 'add_many') as mock:
            self.__manager.add_many(self.__micro_rna_gene_target_dtos)
            assert not mock.called

        self.__fe.result_list = ['hsa-mir-392', 'hsa-mir-32', 'hsa-mir-3921']
        self.__repository.get_many.return_value = self.__fe

        with patch.object(self.__repository, 'add_many') as mock:
            self.__manager.add_many(self.__micro_rna_gene_target_dtos)
            mock.assert_called_with([MicroRnaGeneTargetDto(micro_rna_symbol='hsa-mir-1392',
                                                           id_entrez_genes=[1, 2, 3, 4, 5]),
                                     MicroRnaGeneTargetDto(micro_rna_symbol='hsa-mir-3992',
                                                           id_entrez_genes=[1, 2, 3, 4, 5])])

if __name__ == '__main__':
    unittest.main()
