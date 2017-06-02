import unittest

from Src.BioDataManagement.CrossCutting.DTOs.DnaMethylationLevelDto import DnaMethylationLevelDto


class DnaMethylationLevelDtoTest(unittest.TestCase):
    def test_instance(self):
        dna_methylation_level_dto = DnaMethylationLevelDto(id_entrez=1,
                                                           control_value=0.1,
                                                           case_value=12)

        self.assertEqual(dna_methylation_level_dto.id_entrez, 1)
        self.assertEqual(dna_methylation_level_dto.control_value, 0.1)
        self.assertEqual(dna_methylation_level_dto.case_value, 12)

    def test_properties(self):
        dna_methylation_level_dto = DnaMethylationLevelDto()
        dna_methylation_level_dto.id_entrez = 1
        dna_methylation_level_dto.control_value = 0.1
        dna_methylation_level_dto.case_value = 12

        self.assertEqual(dna_methylation_level_dto.id_entrez, 1)
        self.assertEqual(dna_methylation_level_dto.control_value, 0.1)
        self.assertEqual(dna_methylation_level_dto.case_value, 12)

    def test_equal(self):
        dna_methylation_level_dtos = [DnaMethylationLevelDto(id_entrez=1,
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

        self.assertTrue(len(list(set(dna_methylation_level_dtos))) == 3)

if __name__ == '__main__':
    unittest.main()
