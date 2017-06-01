import unittest

from Src.BioDataFileManagement.CrossCutting.Filters.FeSingleMicroRnaGeneTargetFile import FeSingleMicroRnaGeneTargetFile


class FeSingleMicroRnaGeneTargetFileTest(unittest.TestCase):
    def test_instance(self):
        filter = FeSingleMicroRnaGeneTargetFile(file='microrna_gene_target.txt')
        self.assertEqual(filter.file, 'microrna_gene_target.txt')

    def test_instance_fail(self):
        self.assertRaises(ValueError, FeSingleMicroRnaGeneTargetFile)


if __name__ == '__main__':
    unittest.main()
