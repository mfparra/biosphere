import unittest

from Src.BioDataManagement.DataAccess.Entities.GeneExpressionLevel import GeneExpressionLevel


class GeneExpressionLevelTest(unittest.TestCase):
    def test_instance(self):
        gene_expression_level = GeneExpressionLevel(id_entrez=1,
                                                    control=0.1,
                                                    case=12)

        self.assertEqual(gene_expression_level.id_entrez, 1)
        self.assertEqual(gene_expression_level.control, 0.1)
        self.assertEqual(gene_expression_level.case, 12)

    def test_properties(self):
        gene_expression_level = GeneExpressionLevel()
        gene_expression_level.id_entrez = 1
        gene_expression_level.control = 0.1
        gene_expression_level.case = 12

        self.assertEqual(gene_expression_level.id_entrez, 1)
        self.assertEqual(gene_expression_level.control, 0.1)
        self.assertEqual(gene_expression_level.case, 12)

    def test_equal(self):
        gene_expression_levels = [GeneExpressionLevel(id_entrez=1,
                                                      control=0.1,
                                                      case=12),
                                  GeneExpressionLevel(id_entrez=12,
                                                      control=0.1,
                                                      case=12),
                                  GeneExpressionLevel(id_entrez=1,
                                                      control=0.1,
                                                      case=12),
                                  GeneExpressionLevel(id_entrez=14,
                                                      control=0.1,
                                                      case=12)]

        self.assertTrue(len(list(set(gene_expression_levels))) == 3)

    def test_validation(self):
        gene_expression_level = GeneExpressionLevel()
        gene_expression_level.id_entrez = 1
        gene_expression_level.control = 0.1
        gene_expression_level.case = 12

        try:
            gene_expression_level.validate()
        except ValueError:
            self.fail('Encountered an unexpected exception.')

    def test_validation_fail(self):
        gene_expression_level = GeneExpressionLevel(control=0.1, case=12)
        self.assertRaises(ValueError, gene_expression_level.validate)

        gene_expression_level = GeneExpressionLevel(id_entrez=1, case=12)
        self.assertRaises(ValueError, gene_expression_level.validate)

        gene_expression_level = GeneExpressionLevel(id_entrez=1, control=12)
        self.assertRaises(ValueError, gene_expression_level.validate)

    def test_as_dict(self):
        gene_expression_level = GeneExpressionLevel(id_entrez=1,
                                                    control=0.1,
                                                    case=12)

        gene_expression_level_dict = gene_expression_level.as_dict()

        self.assertTrue('id_entrez' in gene_expression_level_dict)
        self.assertEqual(gene_expression_level_dict['id_entrez'], 1)

        self.assertTrue('control' in gene_expression_level_dict)
        self.assertEqual(gene_expression_level_dict['control'], 0.1)

        self.assertTrue('case' in gene_expression_level_dict)
        self.assertEqual(gene_expression_level_dict['case'], 12)

if __name__ == '__main__':
    unittest.main()
