import unittest

from Src.BioDataManagement.CrossCutting.DTOs.MicroRnaExpressionLevelDto import MicroRnaExpressionLevelDto
from Src.BioDataManagement.CrossCutting.DTOs.MicroRnaSampleDto import MicroRnaSampleDto


class MessengerRnaSampleDtoTest(unittest.TestCase):
    def test_instance(self):
        mirna_sample_dto = MicroRnaSampleDto(patient_id='TCGA-A7-A0DB',
                                             mirna_expression_levels=[MicroRnaExpressionLevelDto(symbol='hsa-mir-1322',
                                                                                                 control_value=0.1,
                                                                                                 case_value=12),
                                                                      MicroRnaExpressionLevelDto(symbol='hsa-mir-1321',
                                                                                                 control_value=0.1,
                                                                                                 case_value=12),
                                                                      MicroRnaExpressionLevelDto(symbol='hsa-mir-1322',
                                                                                                 control_value=0.1,
                                                                                                 case_value=12),
                                                                      MicroRnaExpressionLevelDto(symbol='hsa-mir-0322',
                                                                                                 control_value=0.1,
                                                                                                 case_value=12)])

        self.assertEqual(mirna_sample_dto.patient_id, 'TCGA-A7-A0DB')
        self.assertTrue(len(mirna_sample_dto.mirna_expression_levels) == 3)

    def test_properties(self):
        mirna_sample_dto = MicroRnaSampleDto()
        mirna_sample_dto.patient_id='TCGA-A7-A0DB'
        mirna_sample_dto.mirna_expression_levels=[MicroRnaExpressionLevelDto(symbol='hsa-mir-1322',
                                                                             control_value=0.1,
                                                                             case_value=12),
                                                  MicroRnaExpressionLevelDto(symbol='hsa-mir-1321',
                                                                             control_value=0.1,
                                                                             case_value=12),
                                                  MicroRnaExpressionLevelDto(symbol='hsa-mir-1322',
                                                                             control_value=0.1,
                                                                             case_value=12),
                                                  MicroRnaExpressionLevelDto(symbol='hsa-mir-122',
                                                                             control_value=0.1,
                                                                             case_value=12)]

        self.assertEqual(mirna_sample_dto.patient_id, 'TCGA-A7-A0DB')
        self.assertTrue(len(list(set(mirna_sample_dto.mirna_expression_levels))) == 3)

    def test_equal(self):
        mirna_sample_dtos = [MicroRnaSampleDto(patient_id='TCGA-A7-A0DB',
                                               mirna_expression_levels=[MicroRnaExpressionLevelDto(symbol='hsa-mir-1322',
                                                                                                   control_value=0.1,
                                                                                                   case_value=12),
                                                                        MicroRnaExpressionLevelDto(symbol='hsa-mir-132',
                                                                                                   control_value=0.1,
                                                                                                   case_value=12),
                                                                        MicroRnaExpressionLevelDto(symbol='hsa-mir-1322',
                                                                                                   control_value=0.1,
                                                                                                   case_value=12),
                                                                        MicroRnaExpressionLevelDto(symbol='hsa-mir-322',
                                                                                                   control_value=0.1,
                                                                                                   case_value=12)]),
                             MicroRnaSampleDto(patient_id='TCGA-E7-A0DB',
                                               mirna_expression_levels=[MicroRnaExpressionLevelDto(symbol='hsa-mir-1322',
                                                                                                   control_value=0.1,
                                                                                                   case_value=12),
                                                                        MicroRnaExpressionLevelDto(symbol='hsa-mir-322',
                                                                                                   control_value=0.1,
                                                                                                   case_value=12),
                                                                        MicroRnaExpressionLevelDto(symbol='hsa-mir-1322',
                                                                                                   control_value=0.1,
                                                                                                   case_value=12),
                                                                        MicroRnaExpressionLevelDto(symbol='hsa-mir-132',
                                                                                                   control_value=0.1,
                                                                                                   case_value=12)]),
                             MicroRnaSampleDto(patient_id='TCGA-A3-A0DB',
                                               mirna_expression_levels=[MicroRnaExpressionLevelDto(symbol='hsa-mir-1322',
                                                                                                   control_value=0.1,
                                                                                                   case_value=12),
                                                                        MicroRnaExpressionLevelDto(symbol='hsa-mir-1323',
                                                                                                   control_value=0.1,
                                                                                                   case_value=12),
                                                                        MicroRnaExpressionLevelDto(symbol='hsa-mir-1322',
                                                                                                   control_value=0.1,
                                                                                                   case_value='hsa-mir-322'),
                                                                        MicroRnaExpressionLevelDto(symbol='hsa-mir-132',
                                                                                                   control_value=0.1,
                                                                                                   case_value=12)]),
                             MicroRnaSampleDto(patient_id='TCGA-A7-A0DB',
                                               mirna_expression_levels=[MicroRnaExpressionLevelDto(symbol='hsa-mir-1322',
                                                                                                   control_value=0.1,
                                                                                                   case_value=12),
                                                                        MicroRnaExpressionLevelDto(symbol='hsa-mir-322',
                                                                                                   control_value=0.1,
                                                                                                   case_value=12),
                                                                        MicroRnaExpressionLevelDto(symbol='hsa-mir-1322',
                                                                                                   control_value=0.1,
                                                                                                   case_value=12),
                                                                        MicroRnaExpressionLevelDto(symbol='hsa-mir-132',
                                                                                                   control_value=0.1,
                                                                                                   case_value=12)])]

        self.assertTrue(len(list(set(mirna_sample_dtos))) == 3)

if __name__ == '__main__':
    unittest.main()
