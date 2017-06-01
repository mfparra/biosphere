import unittest

from Src.BioDataManagement.CrossCutting.Filters.FeListMicroRnaGeneTarget import FeListMicroRnaGeneTarget


class FeListMicroRnaGeneTargetTest(unittest.TestCase):
    def test_instance(self):
        filter = FeListMicroRnaGeneTarget(mirna_symbol_list=['hsa-mir-192', 'hsa-mir-312', 'hsa-mir-319', 'hsa-mir-12'])
        self.assertListEqual(filter.mirna_symbol_list, ['hsa-mir-192', 'hsa-mir-312', 'hsa-mir-319', 'hsa-mir-12'])


if __name__ == '__main__':
    unittest.main()
