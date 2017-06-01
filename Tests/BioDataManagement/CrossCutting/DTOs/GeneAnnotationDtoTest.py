import unittest

from Src.BioDataManagement.CrossCutting.DTOs.GeneAnnotationDto import GeneAnnotationDto


class GeneAnnotationDtoTest(unittest.TestCase):
    def test_instance(self):
        gene_annotation_dto = GeneAnnotationDto(id_entrez=1,
                                                symbol='ABC',
                                                synonyms_genes=['CDB', 'AB1', 'DC3'])

        self.assertEqual(gene_annotation_dto.id_entrez, 1)
        self.assertEqual(gene_annotation_dto.symbol, 'ABC')
        self.assertListEqual(gene_annotation_dto.synonyms_genes, ['CDB', 'AB1', 'DC3'])

    def test_properties(self):
        gene_annotation_dto = GeneAnnotationDto()
        gene_annotation_dto.id_entrez = 1
        gene_annotation_dto.symbol = 'ABC'
        gene_annotation_dto.synonyms_genes = ['CDB', 'AB1', 'DC3']

        self.assertEqual(gene_annotation_dto.id_entrez, 1)
        self.assertEqual(gene_annotation_dto.symbol, 'ABC')
        self.assertListEqual(gene_annotation_dto.synonyms_genes, ['CDB', 'AB1', 'DC3'])

    def test_equal(self):
        gene_annotation_dto_list = [GeneAnnotationDto(id_entrez=1,
                                                      symbol='ABC',
                                                      synonyms_genes=['CDB', 'AB1', 'DC3']),
                                    GeneAnnotationDto(id_entrez=2,
                                                      symbol='ABC',
                                                      synonyms_genes=['CDB', 'AB1', 'DC3']),
                                    GeneAnnotationDto(id_entrez=3,
                                                      symbol='AB3',
                                                      synonyms_genes=['CDB', 'AB1', 'DC3']),
                                    GeneAnnotationDto(id_entrez=3,
                                                      symbol='AB3',
                                                      synonyms_genes=['CDB', 'AB1', 'DC3'])]

        self.assertTrue(len(list(set(gene_annotation_dto_list))) == 3)

if __name__ == '__main__':
    unittest.main()
