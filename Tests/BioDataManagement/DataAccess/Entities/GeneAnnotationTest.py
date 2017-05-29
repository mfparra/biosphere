import unittest

from Src.BioDataManagement.DataAccess.Entities.GeneAnnotation import GeneAnnotation


class GeneAnnotationTest(unittest.TestCase):
    def test_instance(self):
        gene_annotation = GeneAnnotation(id_entrez=1,
                                         symbol='ABC',
                                         synonyms_genes=['CDB', 'AB1', 'DC3'])

        self.assertEqual(gene_annotation.id_entrez, 1)
        self.assertEqual(gene_annotation.symbol, 'ABC')
        self.assertListEqual(gene_annotation.synonyms_genes, ['CDB', 'AB1', 'DC3'])

    def test_properties(self):
        gene_annotation = GeneAnnotation()
        gene_annotation.id_entrez = 1
        gene_annotation.symbol = 'ABC'
        gene_annotation.synonyms_genes = ['CDB', 'AB1', 'DC3']

        self.assertEqual(gene_annotation.id_entrez, 1)
        self.assertEqual(gene_annotation.symbol, 'ABC')
        self.assertListEqual(gene_annotation.synonyms_genes, ['CDB', 'AB1', 'DC3'])

    def test_equal(self):
        gene_annotation_list = [GeneAnnotation(id_entrez=1,
                                               symbol='ABC',
                                               synonyms_genes=['CDB', 'AB1', 'DC3']),
                                GeneAnnotation(id_entrez=2,
                                               symbol='ABC',
                                               synonyms_genes=['CDB', 'AB1', 'DC3']),
                                GeneAnnotation(id_entrez=3,
                                               symbol='AB3',
                                               synonyms_genes=['CDB', 'AB1', 'DC3']),
                                GeneAnnotation(id_entrez=3,
                                               symbol='AB3',
                                               synonyms_genes=['CDB', 'AB1', 'DC3'])]

        self.assertTrue(len(list(set(gene_annotation_list))), 3)

    def test_validation(self):
        gene_annotation = GeneAnnotation()
        gene_annotation.id_entrez = 1
        gene_annotation.symbol = 'ABC'
        gene_annotation.synonyms_genes = ['CDB', 'AB1', 'DC3']

        try:
            gene_annotation.validate()
        except ValueError:
            self.fail('Encountered an unexpected exception.')

    def test_validation_fail(self):
        gene_annotation = GeneAnnotation(symbol='ABC',
                                         synonyms_genes=['CDB', 'AB1', 'DC3'])

        self.assertRaises(ValueError, gene_annotation.validate)

        gene_annotation = GeneAnnotation(id_entrez=1,
                                         synonyms_genes=['CDB', 'AB1', 'DC3'])

        self.assertRaises(ValueError, gene_annotation.validate)

        gene_annotation = GeneAnnotation(id_entrez=0,
                                         symbol='ABC',
                                         synonyms_genes=['CDB', 'AB1', 'DC3'])

        self.assertRaises(ValueError, gene_annotation.validate)

    def test_as_dict(self):
        gene_annotation = GeneAnnotation(id_entrez=1,
                                         symbol='ABC',
                                         synonyms_genes=['CDB', 'AB1', 'DC3'])

        gene_annotation_dict = gene_annotation.as_dict()

        self.assertTrue('id_entrez' in gene_annotation_dict)
        self.assertEqual(gene_annotation_dict['id_entrez'], 1)

        self.assertTrue('symbol' in gene_annotation_dict)
        self.assertEqual(gene_annotation_dict['symbol'], 'ABC')

        self.assertTrue('synonyms_genes' in gene_annotation_dict)
        self.assertListEqual(gene_annotation_dict['synonyms_genes'], ['CDB', 'AB1', 'DC3'])

if __name__ == '__main__':
    unittest.main()
