import unittest

from Src.BioDataManagement.DataAccess.Entities.MicroRnaExpressionLevel import MicroRnaExpressionLevel


class MicroRnaExpressionLevelTest(unittest.TestCase):
    def test_instance(self):
        mirna_expression_level = MicroRnaExpressionLevel(symbol='hsa-mir-3192',
                                                         control=0.1,
                                                         case=12)

        self.assertEqual(mirna_expression_level.symbol, 'hsa-mir-3192')
        self.assertEqual(mirna_expression_level.control, 0.1)
        self.assertEqual(mirna_expression_level.case, 12)

    def test_properties(self):
        mirna_expression_level = MicroRnaExpressionLevel()
        mirna_expression_level.symbol = 'hsa-mir-3192'
        mirna_expression_level.control = 0.1
        mirna_expression_level.case = 12

        self.assertEqual(mirna_expression_level.symbol, 'hsa-mir-3192')
        self.assertEqual(mirna_expression_level.control, 0.1)
        self.assertEqual(mirna_expression_level.case, 12)

    def test_equal(self):
        mirna_expression_levels = [MicroRnaExpressionLevel(symbol='hsa-mir-3192',
                                                           control=0.1,
                                                           case=12),
                                   MicroRnaExpressionLevel(symbol='hsa-mir-3191',
                                                           control=0.1,
                                                           case=12),
                                   MicroRnaExpressionLevel(symbol='hsa-mir-3192',
                                                           control=0.1,
                                                           case=12),
                                   MicroRnaExpressionLevel(symbol='hsa-mir-319',
                                                           control=0.1,
                                                           case=12)]

        self.assertTrue(len(list(set(mirna_expression_levels))) == 3)

    def test_validation(self):
        mirna_expression_level = MicroRnaExpressionLevel()
        mirna_expression_level.symbol = 1
        mirna_expression_level.control = 0.1
        mirna_expression_level.case = 12

        try:
            mirna_expression_level.validate()
        except ValueError:
            self.fail('Encountered an unexpected exception.')

    def test_validation_fail(self):
        mirna_expression_level = MicroRnaExpressionLevel(control=0.1, case=12)
        self.assertRaises(ValueError, mirna_expression_level.validate)

        mirna_expression_level = MicroRnaExpressionLevel(symbol='hsa-mir-3192', case=12)
        self.assertRaises(ValueError, mirna_expression_level.validate)

        mirna_expression_level = MicroRnaExpressionLevel(symbol='hsa-mir-3192', control=12)
        self.assertRaises(ValueError, mirna_expression_level.validate)

    def test_as_dict(self):
        mirna_expression_level = MicroRnaExpressionLevel(symbol='hsa-mir-3192',
                                                         control=0.1,
                                                         case=12)

        mirna_expression_level_dict = mirna_expression_level.as_dict()

        self.assertTrue('id_entrez' in mirna_expression_level_dict)
        self.assertEqual(mirna_expression_level_dict['symbol'], 'hsa-mir-3192')

        self.assertTrue('control' in mirna_expression_level_dict)
        self.assertEqual(mirna_expression_level_dict['control'], 0.1)

        self.assertTrue('case' in mirna_expression_level_dict)
        self.assertEqual(mirna_expression_level_dict['case'], 12)

if __name__ == '__main__':
    unittest.main()
