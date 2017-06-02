import unittest

from Src.BioDataManagement.CrossCutting.DTOs.DnaMethylationLevelDto import DnaMethylationLevelDto
from Src.BioDataManagement.CrossCutting.DTOs.DnaMethylationSampleDto import DnaMethylationSampleDto


class MessengerRnaSampleDtoTest(unittest.TestCase):
    def test_instance(self):
        dna_methylation_sample_dto = DnaMethylationSampleDto(patient_id='TCGA-A7-A0DB',
                                                             dna_methylation_levels=[DnaMethylationLevelDto(id_entrez=1,
                                                                                                            control_value=0.1,
                                                                                                            case_value=12),
                                                                                     DnaMethylationLevelDto(id_entrez=12,
                                                                                                            control_value=0.1,
                                                                                                            case_value=12),
                                                                                     DnaMethylationLevelDto(id_entrez=1,
                                                                                                            control_value=0.1,
                                                                                                            case_value=12),
                                                                                     DnaMethylationLevelDto(id_entrez=14,
                                                                                                            control_value=0.1,
                                                                                                            case_value=12)])

        self.assertEqual(dna_methylation_sample_dto.patient_id, 'TCGA-A7-A0DB')
        self.assertTrue(len(dna_methylation_sample_dto.dna_methylation_levels) == 3)

    def test_properties(self):
        dna_methylation_sample_dto = DnaMethylationSampleDto()
        dna_methylation_sample_dto.patient_id='TCGA-A7-A0DB'
        dna_methylation_sample_dto.dna_methylation_levels=[DnaMethylationLevelDto(id_entrez=1,
                                                                                  control_value=0.1,
                                                                                  case_value=12),
                                                           DnaMethylationLevelDto(id_entrez=12,
                                                                                  control_value=0.1,
                                                                                  case_value=12),
                                                           DnaMethylationLevelDto(id_entrez=1,
                                                                                  control_value=0.1,
                                                                                  case_value=12),
                                                           DnaMethylationLevelDto(id_entrez=14,
                                                                                  control_value=0.1,
                                                                                  case_value=12)]

        self.assertEqual(dna_methylation_sample_dto.patient_id, 'TCGA-A7-A0DB')
        self.assertTrue(len(list(set(dna_methylation_sample_dto.dna_methylation_levels))) == 3)

    def test_equal(self):
        dna_methylation_sample_dtos = [DnaMethylationSampleDto(patient_id='TCGA-A7-A0DB',
                                                            dna_methylation_levels=[DnaMethylationLevelDto(id_entrez=1,
                                                                                                         control_value=0.1,
                                                                                                         case_value=12),
                                                                                  DnaMethylationLevelDto(id_entrez=12,
                                                                                                         control_value=0.1,
                                                                                                         case_value=12),
                                                                                  DnaMethylationLevelDto(id_entrez=1,
                                                                                                         control_value=0.1,
                                                                                                         case_value=12),
                                                                                  DnaMethylationLevelDto(id_entrez=14,
                                                                                                         control_value=0.1,
                                                                                                         case_value=12)]),
                                    DnaMethylationSampleDto(patient_id='TCGA-E7-A0DB',
                                                            dna_methylation_levels=[DnaMethylationLevelDto(id_entrez=1,
                                                                                                         control_value=0.1,
                                                                                                         case_value=12),
                                                                                  DnaMethylationLevelDto(id_entrez=12,
                                                                                                         control_value=0.1,
                                                                                                         case_value=12),
                                                                                  DnaMethylationLevelDto(id_entrez=1,
                                                                                                         control_value=0.1,
                                                                                                         case_value=12),
                                                                                  DnaMethylationLevelDto(id_entrez=14,
                                                                                                         control_value=0.1,
                                                                                                         case_value=12)]),
                                    DnaMethylationSampleDto(patient_id='TCGA-A3-A0DB',
                                                            dna_methylation_levels=[DnaMethylationLevelDto(id_entrez=1,
                                                                                                         control_value=0.1,
                                                                                                         case_value=12),
                                                                                  DnaMethylationLevelDto(id_entrez=12,
                                                                                                         control_value=0.1,
                                                                                                         case_value=12),
                                                                                  DnaMethylationLevelDto(id_entrez=1,
                                                                                                         control_value=0.1,
                                                                                                         case_value=12),
                                                                                  DnaMethylationLevelDto(id_entrez=14,
                                                                                                         control_value=0.1,
                                                                                                         case_value=12)]),
                                    DnaMethylationSampleDto(patient_id='TCGA-A7-A0DB',
                                                            dna_methylation_levels=[DnaMethylationLevelDto(id_entrez=1,
                                                                                                         control_value=0.1,
                                                                                                         case_value=12),
                                                                                  DnaMethylationLevelDto(id_entrez=12,
                                                                                                         control_value=0.1,
                                                                                                         case_value=12),
                                                                                  DnaMethylationLevelDto(id_entrez=1,
                                                                                                         control_value=0.1,
                                                                                                         case_value=12),
                                                                                  DnaMethylationLevelDto(id_entrez=14,
                                                                                                         control_value=0.1,
                                                                                                         case_value=12)])]

        self.assertTrue(len(list(set(dna_methylation_sample_dtos))) == 3)

if __name__ == '__main__':
    unittest.main()
