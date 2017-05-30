import unittest
from unittest.mock import Mock, patch

from Src.BioDataManagement.CrossCutting.Contracts.GeneAnnotationRepositoryBase import GeneAnnotationRepositoryBase
from Src.BioDataManagement.CrossCutting.DTOs.GeneAnnotationDto import GeneAnnotationDto
from Src.BioDataManagement.CrossCutting.Filters.FeListGeneAnnotation import FeListGeneAnnotation
from Src.BioDataManagement.Managers.GeneAnnotationManager import GeneAnnotationManager


class GeneAnnotationManagerTests(unittest.TestCase):
    def setUp(self):
        self.__gene_annotation_dtos = [GeneAnnotationDto(id_entrez=1,
                                                         symbol='ABC',
                                                         synonyms_genes=['CDB', 'AB1', 'DC3']),
                                       GeneAnnotationDto(id_entrez=2,
                                                         symbol='AB1',
                                                         synonyms_genes=['CD1', 'AC1', 'DC3']),
                                       GeneAnnotationDto(id_entrez=3,
                                                         symbol='AC3'),
                                       GeneAnnotationDto(id_entrez=6,
                                                         symbol='DA1'),
                                       GeneAnnotationDto(id_entrez=2,
                                                         symbol='AB1',
                                                         synonyms_genes=['CD1', 'AC1', 'DC3'])]

        self.__repository = Mock(spec=GeneAnnotationRepositoryBase)
        self.__fe = FeListGeneAnnotation()
        self.__fe.result_list = [g.id_entrez for g in self.__gene_annotation_dtos[:-1]]

        self.__repository.get_many.return_value  = self.__fe
        self.__manager = GeneAnnotationManager(self.__repository)

    def test_get_many(self):
        fe =  self.__manager.get_many(FeListGeneAnnotation())
        self.assertTrue(len(fe.result_list), 4)

    def test_add_many(self):
        with patch.object(self.__repository, 'add_many') as mock:
            gene_annotations =  self.__manager.add_many(self.__gene_annotation_dtos)
            assert not mock.called

        self.__fe.result_list = [1,2]
        self.__repository.get_many.return_value = self.__fe

        with patch.object(self.__repository, 'add_many') as mock:
            gene_annotations =  self.__manager.add_many(self.__gene_annotation_dtos)
            mock.assert_called_with([GeneAnnotationDto(id_entrez=3,
                                                       symbol='AC3'),
                                     GeneAnnotationDto(id_entrez=6,
                                                       symbol='DA1')])

if __name__ == '__main__':
    unittest.main()
