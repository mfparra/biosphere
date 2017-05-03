import unittest

from Src.BioDataFileManagement.CrossCutting.Filters.FeSingleGeneAnnotation import FeSingleGeneAnnotation


class FeSingleGeneAnnotationTests(unittest.TestCase):
    def test_instance(self):
        filter = FeSingleGeneAnnotation(file='gene_annotation.txt')
        self.assertEqual(filter.file, 'gene_annotation.txt')

    def test_instance_fail(self):
        self.assertRaises(ValueError, FeSingleGeneAnnotation)


if __name__ == '__main__':
    unittest.main()
