import unittest

from Src.BioDataManagement.CrossCutting.DTOs.MicroRnaExpressionLevelDto import MicroRnaExpressionLevelDto


class MicroRnaExpressionLevelDtoTest(unittest.TestCase):
    def test_instance(self):
        micro_rna_expression_level_dto = MicroRnaExpressionLevelDto(symbol='hsa-mir-1322',
                                                                    control_value=0.1,
                                                                    case_value=12)

        self.assertEqual(micro_rna_expression_level_dto.symbol, 'hsa-mir-1322')
        self.assertEqual(micro_rna_expression_level_dto.control_value, 0.1)
        self.assertEqual(micro_rna_expression_level_dto.case_value, 12)

    def test_properties(self):
        micro_rna_expression_level_dto = MicroRnaExpressionLevelDto()
        micro_rna_expression_level_dto.symbol = 'hsa-mir-1322'
        micro_rna_expression_level_dto.control_value = 0.1
        micro_rna_expression_level_dto.case_value = 12

        self.assertEqual(micro_rna_expression_level_dto.symbol, 'hsa-mir-1322')
        self.assertEqual(micro_rna_expression_level_dto.control_value, 0.1)
        self.assertEqual(micro_rna_expression_level_dto.case_value, 12)

    def test_equal(self):
        micro_rna_expression_level_dtos = [MicroRnaExpressionLevelDto(symbol='hsa-mir-1322',
                                                                      control_value=0.1,
                                                                      case_value=12),
                                           MicroRnaExpressionLevelDto(symbol='hsa-mir-1321',
                                                                      control_value=0.1,
                                                                      case_value=12),
                                           MicroRnaExpressionLevelDto(symbol='hsa-mir-1322',
                                                                      control_value=0.1,
                                                                      case_value=12),
                                           MicroRnaExpressionLevelDto(symbol='hsa-mir-1122',
                                                                      control_value=0.1,
                                                                      case_value=12)]

        self.assertTrue(len(list(set(micro_rna_expression_level_dtos))) == 3)

if __name__ == '__main__':
    unittest.main()
