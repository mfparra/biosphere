import unittest

from Src.BioDataFileManagement.CrossCutting.Filters.FeSingleMicroRnaGeneTarget import FeSingleMicroRnaGeneTarget


class FeSingleMicroRnaGeneTargetTests(unittest.TestCase):
    def test_instance(self):
        filter = FeSingleMicroRnaGeneTarget(file='microrna_gene_target.txt')
        self.assertEqual(filter.file, 'microrna_gene_target.txt')

    def test_instance_fail(self):
        self.assertRaises(ValueError, FeSingleMicroRnaGeneTarget)


if __name__ == '__main__':
    unittest.main()
