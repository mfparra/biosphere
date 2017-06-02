import unittest

from Src.BioDataManagement.DataAccess.Entities.DnaMethylationLevel import DnaMethylationLevel


class DnaMethylationLevelTest(unittest.TestCase):
    def test_instance(self):
        dna_methylation_level = DnaMethylationLevel(id_entrez=1,
                                                    control=0.1,
                                                    case=12)

        self.assertEqual(dna_methylation_level.id_entrez, 1)
        self.assertEqual(dna_methylation_level.control, 0.1)
        self.assertEqual(dna_methylation_level.case, 12)

    def test_properties(self):
        dna_methylation_level = DnaMethylationLevel()
        dna_methylation_level.id_entrez = 1
        dna_methylation_level.control = 0.1
        dna_methylation_level.case = 12

        self.assertEqual(dna_methylation_level.id_entrez, 1)
        self.assertEqual(dna_methylation_level.control, 0.1)
        self.assertEqual(dna_methylation_level.case, 12)

    def test_equal(self):
        dna_methylation_levels = [DnaMethylationLevel(id_entrez=1,
                                                      control=0.1,
                                                      case=12),
                                  DnaMethylationLevel(id_entrez=12,
                                                      control=0.1,
                                                      case=12),
                                  DnaMethylationLevel(id_entrez=1,
                                                      control=0.1,
                                                      case=12),
                                  DnaMethylationLevel(id_entrez=14,
                                                      control=0.1,
                                                      case=12)]

        self.assertTrue(len(list(set(dna_methylation_levels))) == 3)

    def test_validation(self):
        dna_methylation_level = DnaMethylationLevel()
        dna_methylation_level.id_entrez = 1
        dna_methylation_level.control = 0.1
        dna_methylation_level.case = 12

        try:
            dna_methylation_level.validate()
        except ValueError:
            self.fail('Encountered an unexpected exception.')

    def test_validation_fail(self):
        dna_methylation_level = DnaMethylationLevel(control=0.1, case=12)
        self.assertRaises(ValueError, dna_methylation_level.validate)

        dna_methylation_level = DnaMethylationLevel(id_entrez=1, case=12)
        self.assertRaises(ValueError, dna_methylation_level.validate)

        dna_methylation_level = DnaMethylationLevel(id_entrez=1, control=12)
        self.assertRaises(ValueError, dna_methylation_level.validate)

    def test_as_dict(self):
        dna_methylation_level = DnaMethylationLevel(id_entrez=1,
                                                    control=0.1,
                                                    case=12)

        dna_methylation_level_dict = dna_methylation_level.as_dict()

        self.assertTrue('id_entrez' in dna_methylation_level_dict)
        self.assertEqual(dna_methylation_level_dict['id_entrez'], 1)

        self.assertTrue('control' in dna_methylation_level_dict)
        self.assertEqual(dna_methylation_level_dict['control'], 0.1)

        self.assertTrue('case' in dna_methylation_level_dict)
        self.assertEqual(dna_methylation_level_dict['case'], 12)

if __name__ == '__main__':
    unittest.main()
