import unittest

from Src.BioDataManagement.CrossCutting.DTOs.GeneAnnotationDto import GeneAnnotationDto
from Src.BioDataManagement.DataAccess.Entities.GeneAnnotation import GeneAnnotation
from Src.BioDataManagement.DataAccess.Mappers.Mapper import Mapper


class MapperTest(unittest.TestCase):

    def test_map(self):
        gene_annotation = Mapper.get_instance().map(GeneAnnotationDto(id_entrez=1,
                                                                      symbol='ABC',
                                                                      synonyms_genes=['CDB', 'AB1', 'DC3']),
                                                    GeneAnnotation)

        self.assertEqual(gene_annotation, GeneAnnotation(id_entrez=1,
                                                         symbol='ABC',
                                                         synonyms_genes=['CDB', 'AB1', 'DC3']))

if __name__ == '__main__':
    unittest.main()
