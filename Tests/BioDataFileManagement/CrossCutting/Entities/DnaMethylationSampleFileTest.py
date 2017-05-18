import unittest

from Src.BioDataFileManagement.CrossCutting.Entities.DnaMethylationLevel import DnaMethylationLevel
from Src.BioDataFileManagement.CrossCutting.Entities.DnaMethylationSampleFile import DnaMethylationSampleFile


class DnaMethylationSampleFileTest(unittest.TestCase):
    def test_instance(self):
        dna_methylation_sample_file = DnaMethylationSampleFile(
                                            patient_id='TCGA-A7-A0DC',
                                            dna_methylation_levels=[DnaMethylationLevel(gene_symbol='ABCD',
                                                                                        control_value=12.23,
                                                                                        case_value=32.1213)])

        self.assertEqual(dna_methylation_sample_file.patient_id, 'TCGA-A7-A0DC')
        self.assertEqual(len(dna_methylation_sample_file.dna_methylation_levels), 1)
        self.assertEqual(dna_methylation_sample_file.dna_methylation_levels[0].gene_symbol, 'ABCD')
        self.assertEqual(dna_methylation_sample_file.dna_methylation_levels[0].control_value, 12.23)
        self.assertEqual(dna_methylation_sample_file.dna_methylation_levels[0].case_value, 32.1213)

    def test_instance_fail(self):
        self.assertRaises(ValueError, DnaMethylationSampleFile)
        self.assertRaises(ValueError, DnaMethylationSampleFile, **{'patient_id':'TCGA-A7-A0DC'})

    def test_equal(self):
        dna_methylation_levels = [DnaMethylationSampleFile(patient_id='TCGA-A7-A0DC',
                                                           dna_methylation_levels=[DnaMethylationLevel(
                                                                                        gene_symbol='ABCD',
                                                                                        control_value=12.23,
                                                                                        case_value=32.1213)]),
                                  DnaMethylationSampleFile(patient_id='TCGA-BH-A0AU',
                                                           dna_methylation_levels=[DnaMethylationLevel(
                                                                                        gene_symbol='ABCD',
                                                                                        control_value=12.23,
                                                                                        case_value=32.1213)]),
                                  DnaMethylationSampleFile(patient_id='TCGA-A7-A0DC',
                                                           dna_methylation_levels=[DnaMethylationLevel(
                                                                                        gene_symbol='ABCD',
                                                                                        control_value=12.23,
                                                                                        case_value=32.1213)]),
                                  DnaMethylationSampleFile(patient_id='TCGA-BH-A1EW',
                                                           dna_methylation_levels=[DnaMethylationLevel(
                                                                                        gene_symbol='ABCD',
                                                                                        control_value=12.23,
                                                                                        case_value=32.1213)])]

        self.assertEqual(len(list(set(dna_methylation_levels))), 3)

if __name__ == '__main__':
    unittest.main()
