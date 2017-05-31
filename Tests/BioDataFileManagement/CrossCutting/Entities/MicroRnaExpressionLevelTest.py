import unittest

from Src.BioDataFileManagement.CrossCutting.Entities.MicroRnaExpressionLevel import MicroRnaExpressionLevel


class MicroRnaExpressionLevelTest(unittest.TestCase):
    def test_instance(self):
        mirna_expression_level = MicroRnaExpressionLevel(symbol='hsa-mir-1322',
                                                         control_value=0,
                                                         case_value=32.1213)

        self.assertEqual(mirna_expression_level.symbol, 'hsa-mir-1322')
        self.assertEqual(mirna_expression_level.control_value, 0)
        self.assertEqual(mirna_expression_level.case_value, 32.1213)

    def test_instance_fail(self):
        self.assertRaises(ValueError, MicroRnaExpressionLevel)
        self.assertRaises(ValueError, MicroRnaExpressionLevel, **{'symbol':'abc', 'control_value': 12.23})
        self.assertRaises(ValueError, MicroRnaExpressionLevel, **{'symbol':'abc', 'case_value': 12.23})

    def test_equal(self):
        mirna_expression_levels = [MicroRnaExpressionLevel(symbol='hsa-mir-1322',
                                                           control_value=11,
                                                           case_value=12.23),
                                   MicroRnaExpressionLevel(symbol='hsa-mir-1322',
                                                           control_value=11,
                                                           case_value=12.23),
                                   MicroRnaExpressionLevel(symbol='hsa-mir-132',
                                                           control_value=22,
                                                           case_value=12.23),
                                   MicroRnaExpressionLevel(symbol='hsa-mir-1122',
                                                           control_value=22,
                                                           case_value=12.23)]

        self.assertEqual(len(list(set(mirna_expression_levels))), 3)

if __name__ == '__main__':
    unittest.main()
