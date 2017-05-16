import unittest

from Src.BioDataFileManagement.CrossCutting.Entities.GeneAnnotationFile import GeneAnnotationFile


class GeneAnntationFileTest(unittest.TestCase):
    def test_instance(self):
        gene_annotations = [GeneAnnotationFile(id_entrez=10,
                                               symbol='abc',
                                               synonyms_genes=None),
                            GeneAnnotationFile(id_entrez=14,
                                               symbol='fha',
                                               synonyms_genes=['abd', 'rhj'])]

        self.assertEqual(gene_annotations[0].id_entrez, 10)
        self.assertEqual(gene_annotations[0].symbol, 'ABC')
        self.assertEqual(gene_annotations[0].synonyms_genes, [])

        self.assertListEqual(gene_annotations[1].synonyms_genes, ['ABD', 'RHJ'])

    def test_instance_fail(self):
        self.assertRaises(ValueError, GeneAnnotationFile)
        self.assertRaises(ValueError, GeneAnnotationFile, **{'symbol':'abc', 'synonyms_genes': None})
        self.assertRaises(ValueError, GeneAnnotationFile, **{'id_entrez': 10, 'synonyms_genes': None})

    def test_equal(self):
        gene_annotations = [GeneAnnotationFile(id_entrez=10,
                                               symbol='abc',
                                               synonyms_genes=None),
                            GeneAnnotationFile(id_entrez=14,
                                               symbol='fha',
                                               synonyms_genes=['abd', 'rhj']),
                            GeneAnnotationFile(id_entrez=10,
                                               symbol='abc',
                                               synonyms_genes=None),
                            GeneAnnotationFile(id_entrez=14,
                                               symbol='fha',
                                               synonyms_genes=['abd', 'rhj'])]

        self.assertEqual(len(list(set(gene_annotations))), 2)

if __name__ == '__main__':
    unittest.main()
