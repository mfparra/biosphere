import unittest

from Src.BioDataFileManagement.CrossCutting.Entities.DnaMethylationLevel import DnaMethylationLevel


class DnaMethylationLevelTest(unittest.TestCase):
    def test_instance(self):
        dna_methylation_level = DnaMethylationLevel(gene_symbol='ABCD',
                                                    control_value=12.23,
                                                    case_value=32.1213)

        self.assertEqual(dna_methylation_level.gene_symbol, 'ABCD')
        self.assertEqual(dna_methylation_level.control_value, 12.23)
        self.assertEqual(dna_methylation_level.case_value, 32.1213)

    def test_instance_fail(self):
        self.assertRaises(ValueError, DnaMethylationLevel)
        self.assertRaises(ValueError, DnaMethylationLevel, **{'gene_symbol':'abc', 'control_value': 12.23})
        self.assertRaises(ValueError, DnaMethylationLevel, **{'gene_symbol':'abc', 'case_value': 12.23})

    def test_equal(self):
        dna_methylation_levels = [DnaMethylationLevel(gene_symbol='sdf',
                                                      control_value=11,
                                                      case_value=12.23),
                                  DnaMethylationLevel(gene_symbol='sdf',
                                                      control_value=11,
                                                      case_value=12.23),
                                  DnaMethylationLevel(gene_symbol='abc',
                                                      control_value=22,
                                                      case_value=12.23),
                                  DnaMethylationLevel(gene_symbol='acv',
                                                      control_value=22,
                                                      case_value=12.23)]

        self.assertEqual(len(list(set(dna_methylation_levels))), 3)

if __name__ == '__main__':
    unittest.main()
