import unittest

from Src.BioDataManagement.DataAccess.Entities.GeneExpressionLevel import GeneExpressionLevel
from Src.BioDataManagement.DataAccess.Entities.MessengerRnaSample import MessengerRnaSample


class MessengerRnaSampleTest(unittest.TestCase):
    def test_instance(self):
        messenger_rna_sample = MessengerRnaSample(patient_id='TCGA-A7-A0DB',
                                                  exp_levels=[GeneExpressionLevel(id_entrez=1, control=0.1, case=12),
                                                              GeneExpressionLevel(id_entrez=12, control=0.1, case=12),
                                                              GeneExpressionLevel(id_entrez=1, control=0.1, case=12),
                                                              GeneExpressionLevel(id_entrez=14, control=0.1, case=12)])

        self.assertEqual(messenger_rna_sample.patient_id, 'TCGA-A7-A0DB')
        self.assertTrue(len(messenger_rna_sample.exp_levels) == 3)

    def test_properties(self):
        messenger_rna_sample = MessengerRnaSample()
        messenger_rna_sample.patient_id='TCGA-A7-A0DB'
        messenger_rna_sample.exp_levels=[GeneExpressionLevel(id_entrez=1, control=0.1, case=12),
                                         GeneExpressionLevel(id_entrez=12, control=0.1, case=12),
                                         GeneExpressionLevel(id_entrez=1, control=0.1, case=12),
                                         GeneExpressionLevel(id_entrez=14, control=0.1, case=12)]

        self.assertEqual(messenger_rna_sample.patient_id, 'TCGA-A7-A0DB')
        self.assertTrue(len(messenger_rna_sample.exp_levels) == 3)

    def test_equal(self):
        messenger_rna_sample = [MessengerRnaSample(patient_id='TCGA-A7-A0DB',
                                                   exp_levels=[GeneExpressionLevel(id_entrez=1, control=0.1, case=12),
                                                               GeneExpressionLevel(id_entrez=1, control=0.1, case=12),
                                                               GeneExpressionLevel(id_entrez=1, control=0.1, case=12),
                                                               GeneExpressionLevel(id_entrez=1, control=0.1, case=12)]),
                                MessengerRnaSample(patient_id='TCGA-E7-A0DB',
                                                   exp_levels=[GeneExpressionLevel(id_entrez=1, control=0.1, case=12),
                                                               GeneExpressionLevel(id_entrez=1, control=0.1, case=12),
                                                               GeneExpressionLevel(id_entrez=1, control=0.1, case=12),
                                                               GeneExpressionLevel(id_entrez=1, control=0.1, case=12)]),
                                MessengerRnaSample(patient_id='TCGA-A3-A0DB',
                                                   exp_levels=[GeneExpressionLevel(id_entrez=1, control=0.1, case=12),
                                                               GeneExpressionLevel(id_entrez=1, control=0.1, case=12),
                                                               GeneExpressionLevel(id_entrez=1, control=0.1, case=12),
                                                               GeneExpressionLevel(id_entrez=1, control=0.1, case=12)]),
                                MessengerRnaSample(patient_id='TCGA-A7-A0DB',
                                                   exp_levels=[GeneExpressionLevel(id_entrez=1, control=0.1, case=12),
                                                               GeneExpressionLevel(id_entrez=1, control=0.1, case=12),
                                                               GeneExpressionLevel(id_entrez=1, control=0.1, case=12),
                                                               GeneExpressionLevel(id_entrez=1, control=0.1, case=12)])]

        self.assertTrue(len(list(set(messenger_rna_sample))) == 3)

    def test_validation(self):
        gene_expression_level = GeneExpressionLevel()
        gene_expression_level.id_entrez = 1
        gene_expression_level.control = 0.1
        gene_expression_level.case = 12

        try:
            gene_expression_level.validate()
        except ValueError:
            self.fail('Encountered an unexpected exception.')

    def test_validation_fail(self):
        gene_expression_level = GeneExpressionLevel(control=0.1, case=12)
        self.assertRaises(ValueError, gene_expression_level.validate)

        gene_expression_level = GeneExpressionLevel(id_entrez=1, case=12)
        self.assertRaises(ValueError, gene_expression_level.validate)

        gene_expression_level = GeneExpressionLevel(id_entrez=1, control=12)
        self.assertRaises(ValueError, gene_expression_level.validate)

    def test_as_dict(self):
        gene_expression_level = GeneExpressionLevel(id_entrez=1,
                                                    control=0.1,
                                                    case=12)

        gene_expression_level_dict = gene_expression_level.as_dict()

        self.assertTrue('id_entrez' in gene_expression_level_dict)
        self.assertEqual(gene_expression_level_dict['id_entrez'], 1)

        self.assertTrue('control' in gene_expression_level_dict)
        self.assertEqual(gene_expression_level_dict['control'], 0.1)

        self.assertTrue('case' in gene_expression_level_dict)
        self.assertEqual(gene_expression_level_dict['case'], 12)

if __name__ == '__main__':
    unittest.main()
