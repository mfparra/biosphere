import unittest

from Src.BioDataManagement.CrossCutting.DTOs.GeneExpressionLevelDto import GeneExpressionLevelDto
from Src.BioDataManagement.CrossCutting.DTOs.MessengerRnaSampleDto import MessengerRnaSampleDto


class MessengerRnaSampleDtoTest(unittest.TestCase):
    def test_instance(self):
        messenger_rna_sample_dto = MessengerRnaSampleDto(patient_id='TCGA-A7-A0DB',
                                                         gene_expression_levels=[GeneExpressionLevelDto(id_entrez=1,
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
                                                                                                        case_value=12)])

        self.assertEqual(messenger_rna_sample_dto.patient_id, 'TCGA-A7-A0DB')
        self.assertTrue(len(messenger_rna_sample_dto.gene_expression_levels) == 3)

    def test_properties(self):
        messenger_rna_sample_dto = MessengerRnaSampleDto()
        messenger_rna_sample_dto.patient_id='TCGA-A7-A0DB'
        messenger_rna_sample_dto.gene_expression_levels=[GeneExpressionLevelDto(id_entrez=1,
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

        self.assertEqual(messenger_rna_sample_dto.patient_id, 'TCGA-A7-A0DB')
        self.assertTrue(len(messenger_rna_sample_dto.gene_expression_levels) == 3)

    def test_equal(self):
        messenger_rna_sample_dto = [MessengerRnaSampleDto(patient_id='TCGA-A7-A0DB',
                                                          gene_expression_levels=[GeneExpressionLevelDto(id_entrez=1,
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
                                                                                                         case_value=12)]),
                                    MessengerRnaSampleDto(patient_id='TCGA-E7-A0DB',
                                                          gene_expression_levels=[GeneExpressionLevelDto(id_entrez=1,
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
                                                                                                         case_value=12)]),
                                    MessengerRnaSampleDto(patient_id='TCGA-A3-A0DB',
                                                          gene_expression_levels=[GeneExpressionLevelDto(id_entrez=1,
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
                                                                                                         case_value=12)]),
                                    MessengerRnaSampleDto(patient_id='TCGA-A7-A0DB',
                                                          gene_expression_levels=[GeneExpressionLevelDto(id_entrez=1,
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
                                                                                                         case_value=12)])]

        self.assertTrue(len(list(set(messenger_rna_sample_dto))) == 3)

if __name__ == '__main__':
    unittest.main()
