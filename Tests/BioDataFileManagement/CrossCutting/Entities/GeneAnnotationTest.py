import unittest

from Src.BioDataFileManagement.CrossCutting.Entities.GeneAnnotation import GeneAnnotation


class MyTestCase(unittest.TestCase):
    def test_instance(self):
        gene_annotations = [GeneAnnotation(id_entrez=10,
                                           symbol='abc',
                                           synonyms_genes=None),
                            GeneAnnotation(id_entrez=14,
                                           symbol='fha',
                                           synonyms_genes=['abd', 'rhj'])]

        self.assertEqual(gene_annotations[0].id_entrez, 10)
        self.assertEqual(gene_annotations[0].symbol, 'ABC')
        self.assertEqual(gene_annotations[0].synonyms_genes, [])

        self.assertListEqual(gene_annotations[1].synonyms_genes, ['ABD', 'RHJ'])


if __name__ == '__main__':
    unittest.main()
