import unittest

from Src.BioDataManagement.CrossCutting.DTOs.GeneExpressionLevelDto import GeneExpressionLevelDto


class GeneExpressionLevelDtoTest(unittest.TestCase):
    def test_instance(self):
        gene_expression_level_dto = GeneExpressionLevelDto(id_entrez=1,
                                                           control_value=0.1,
                                                           case_value=12)

        self.assertEqual(gene_expression_level_dto.id_entrez, 1)
        self.assertEqual(gene_expression_level_dto.control_value, 0.1)
        self.assertEqual(gene_expression_level_dto.case_value, 12)

    def test_properties(self):
        gene_expression_level_dto = GeneExpressionLevelDto()
        gene_expression_level_dto.id_entrez = 1
        gene_expression_level_dto.control_value = 0.1
        gene_expression_level_dto.case_value = 12

        self.assertEqual(gene_expression_level_dto.id_entrez, 1)
        self.assertEqual(gene_expression_level_dto.control_value, 0.1)
        self.assertEqual(gene_expression_level_dto.case_value, 12)

    def test_equal(self):
        gene_expression_levels_dto = [GeneExpressionLevelDto(id_entrez=1,
                                                             control_value=0.1,
                                                             case_value=12),
                                      GeneExpressionLevelDto(id_entrez=12,
                                                             control_value=0.1,
                                                             case_value=12),
                                      GeneExpressionLevelDto(id_entrez=1,
                                                             control_value=0.1,
                                                             case_value=12),
                                      GeneExpressionLevelDto(id_entrez=14,
                                                             control_value=0.1,
                                                             case_value=12)]

        self.assertTrue(len(list(set(gene_expression_levels_dto))) == 3)

if __name__ == '__main__':
    unittest.main()
