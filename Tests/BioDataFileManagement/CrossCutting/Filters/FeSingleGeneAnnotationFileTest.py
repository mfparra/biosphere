import unittest

from Src.BioDataFileManagement.CrossCutting.Filters.FeSingleGeneAnnotationFile import FeSingleGeneAnnotationFile


class FeSingleGeneAnnotationFileTests(unittest.TestCase):
    def test_instance(self):
        filter = FeSingleGeneAnnotationFile(file='gene_annotation.txt')
        self.assertEqual(filter.file, 'gene_annotation.txt')

    def test_instance_fail(self):
        self.assertRaises(ValueError, FeSingleGeneAnnotationFile)


if __name__ == '__main__':
    unittest.main()
