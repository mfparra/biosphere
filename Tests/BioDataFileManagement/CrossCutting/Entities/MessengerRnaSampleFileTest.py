import unittest

from Src.BioDataFileManagement.CrossCutting.Entities.GeneExpressionLevel import GeneExpressionLevel
from Src.BioDataFileManagement.CrossCutting.Entities.MessengerRnaSampleFile import MessengerRnaSampleFile


class MessengerRnaSampleFileTest(unittest.TestCase):
    def test_instance(self):
        mrna_sample_file = MessengerRnaSampleFile(patient_id='TCGA-A7-A0DC',
                                                  gene_expression_levels=[GeneExpressionLevel(gene_symbol='ABCD',
                                                                                              control_value=12.23,
                                                                                              case_value=32.1213)])

        self.assertEqual(mrna_sample_file.patient_id, 'TCGA-A7-A0DC')
        self.assertEqual(len(mrna_sample_file.gene_expression_levels), 1)
        self.assertEqual(mrna_sample_file.gene_expression_levels[0].gene_symbol, 'ABCD')
        self.assertEqual(mrna_sample_file.gene_expression_levels[0].control_value, 12.23)
        self.assertEqual(mrna_sample_file.gene_expression_levels[0].case_value, 32.1213)

    def test_instance_fail(self):
        self.assertRaises(ValueError, MessengerRnaSampleFile)
        self.assertRaises(ValueError, MessengerRnaSampleFile, **{'patient_id':'TCGA-A7-A0DC'})

    def test_equal(self):
        gene_expression_levels = [MessengerRnaSampleFile(patient_id='TCGA-A7-A0DC',
                                                         gene_expression_levels=[GeneExpressionLevel(
                                                                                        gene_symbol='ABCD',
                                                                                        control_value=12.23,
                                                                                        case_value=32.1213)]),
                                  MessengerRnaSampleFile(patient_id='TCGA-BH-A0AU',
                                                         gene_expression_levels=[GeneExpressionLevel(
                                                                                        gene_symbol='ABCD',
                                                                                        control_value=12.23,
                                                                                        case_value=32.1213)]),
                                  MessengerRnaSampleFile(patient_id='TCGA-A7-A0DC',
                                                         gene_expression_levels=[GeneExpressionLevel(
                                                                                        gene_symbol='ABCD',
                                                                                        control_value=12.23,
                                                                                        case_value=32.1213)]),
                                  MessengerRnaSampleFile(patient_id='TCGA-BH-A1EW',
                                                         gene_expression_levels=[GeneExpressionLevel(
                                                                                        gene_symbol='ABCD',
                                                                                        control_value=12.23,
                                                                                        case_value=32.1213)])]

        self.assertEqual(len(list(set(gene_expression_levels))), 3)

if __name__ == '__main__':
    unittest.main()
