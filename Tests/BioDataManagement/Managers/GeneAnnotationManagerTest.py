import unittest
from unittest.mock import Mock

from Src.BioDataManagement.CrossCutting.Contracts.GeneAnnotationRepositoryBase import GeneAnnotationRepositoryBase
from Src.BioDataManagement.CrossCutting.DTOs.GeneAnnotationDto import GeneAnnotationDto
from Src.BioDataManagement.CrossCutting.Filters.FeListGeneAnnotation import FeListGeneAnnotation
from Src.BioDataManagement.Managers.GeneAnnotationManager import GeneAnnotationManager


class GeneAnnotationManagerTests(unittest.TestCase):
    def setUp(self):
        repository = Mock(spec=GeneAnnotationRepositoryBase)
        repository.get_many.return_value  = [GeneAnnotationDto(id_entrez=1,
                                                                      symbol='ABC',
                                                                      synonyms_genes=['CDB', 'AB1', 'DC3']),
                                                    GeneAnnotationDto(id_entrez=2,
                                                                      symbol='AB1',
                                                                      synonyms_genes=['CD1', 'AC1', 'DC3']),
                                                    GeneAnnotationDto(id_entrez=3,
                                                                      symbol='AC3'),
                                                    GeneAnnotationDto(id_entrez=1,
                                                                      symbol='BC5',
                                                                      synonyms_genes=['CDB', 'AB1', 'DC3']),
                                                    GeneAnnotationDto(id_entrez=6,
                                                                      symbol='DA1')]

        self.__manager = GeneAnnotationManager(repository)

    def test_get_many(self):
        gene_annotations = self.__manager.get_many(FeListGeneAnnotation())
        self.assertTrue(len(gene_annotations), 3)

if __name__ == '__main__':
    unittest.main()
