import unittest

from Src.BioDataFileManagement.CrossCutting.Entities.GeneExpressionLevel import GeneExpressionLevel


class GeneExpressionLevelTest(unittest.TestCase):
    def test_instance(self):
        gene_expression_level = GeneExpressionLevel(gene_symbol='ABCD',
                                                    control_value=12.23,
                                                    case_value=32.1213)

        self.assertEqual(gene_expression_level.gene_symbol, 'ABCD')
        self.assertEqual(gene_expression_level.control_value, 12.23)
        self.assertEqual(gene_expression_level.case_value, 32.1213)

    def test_instance_fail(self):
        self.assertRaises(ValueError, GeneExpressionLevel)
        self.assertRaises(ValueError, GeneExpressionLevel, **{'gene_symbol':'abc', 'control_value': 12.23})
        self.assertRaises(ValueError, GeneExpressionLevel, **{'gene_symbol':'abc', 'case_value': 12.23})

    def test_equal(self):
        gene_expression_levels = [GeneExpressionLevel(gene_symbol='sdf',
                                                      control_value=11,
                                                      case_value=12.23),
                                  GeneExpressionLevel(gene_symbol='sdf',
                                                      control_value=11,
                                                      case_value=12.23),
                                  GeneExpressionLevel(gene_symbol='abc',
                                                      control_value=22,
                                                      case_value=12.23),
                                  GeneExpressionLevel(gene_symbol='acv',
                                                      control_value=22,
                                                      case_value=12.23)]

        self.assertEqual(len(list(set(gene_expression_levels))), 3)

if __name__ == '__main__':
    unittest.main()
