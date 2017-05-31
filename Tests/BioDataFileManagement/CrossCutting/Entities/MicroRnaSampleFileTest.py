import unittest

from Src.BioDataFileManagement.CrossCutting.Entities.MicroRnaExpressionLevel import MicroRnaExpressionLevel
from Src.BioDataFileManagement.CrossCutting.Entities.MicroRnaSampleFile import MicroRnaSampleFile


class MessengerRnaSampleFileTest(unittest.TestCase):
    def test_instance(self):
        mirna_sample_file = MicroRnaSampleFile(patient_id='TCGA-A7-A0DC',
                                               micro_rna_expression_levels=[MicroRnaExpressionLevel(symbol='hsa-mir-1322',
                                                                                                    control_value=12.23,
                                                                                                    case_value=32.1213)])

        self.assertEqual(mirna_sample_file.patient_id, 'TCGA-A7-A0DC')
        self.assertEqual(len(mirna_sample_file.micro_rna_expression_levels), 1)
        self.assertEqual(mirna_sample_file.micro_rna_expression_levels[0].symbol, 'hsa-mir-1322')
        self.assertEqual(mirna_sample_file.micro_rna_expression_levels[0].control_value, 12.23)
        self.assertEqual(mirna_sample_file.micro_rna_expression_levels[0].case_value, 32.1213)

    def test_instance_fail(self):
        self.assertRaises(ValueError, MicroRnaSampleFile)
        self.assertRaises(ValueError, MicroRnaSampleFile, **{'patient_id':'TCGA-A7-A0DC'})

    def test_equal(self):
        mirna_expression_samples = [MicroRnaSampleFile(patient_id='TCGA-A7-A0DC',
                                                       micro_rna_expression_levels=[MicroRnaExpressionLevel(
                                                                                        symbol='hsa-mir-1322',
                                                                                        control_value=12.23,
                                                                                        case_value=32.1213)]),
                                    MicroRnaSampleFile(patient_id='TCGA-BH-A0AU',
                                                       micro_rna_expression_levels=[MicroRnaExpressionLevel(
                                                                                        symbol='hsa-mir-122',
                                                                                        control_value=12.23,
                                                                                        case_value=32.1213)]),
                                    MicroRnaSampleFile(patient_id='TCGA-A7-A0DC',
                                                       micro_rna_expression_levels=[MicroRnaExpressionLevel(
                                                                                        symbol='hsa-mir-1322',
                                                                                        control_value=12.23,
                                                                                        case_value=32.1213)]),
                                    MicroRnaSampleFile(patient_id='TCGA-BH-A1EW',
                                                       micro_rna_expression_levels=[MicroRnaExpressionLevel(
                                                                                        symbol='hsa-mir-1320',
                                                                                        control_value=12.23,
                                                                                        case_value=32.1213)])]

        self.assertEqual(len(list(set(mirna_expression_samples))), 3)

if __name__ == '__main__':
    unittest.main()
