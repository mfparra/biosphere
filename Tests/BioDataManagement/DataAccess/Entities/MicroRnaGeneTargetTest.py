import unittest

from Src.BioDataManagement.DataAccess.Entities.MicroRnaGeneTarget import MicroRnaGeneTarget


class MicroRnaGeneTargetTest(unittest.TestCase):
    def test_instance(self):
        micro_rna_gene_target = MicroRnaGeneTarget(micro_rna_symbol='hsa-mir-3192',
                                                   id_entrez_genes=[1,2,3,4,5])

        self.assertEqual(micro_rna_gene_target.micro_rna_symbol, 'hsa-mir-3192')
        self.assertListEqual(micro_rna_gene_target.id_entrez_genes, [1,2,3,4,5])

    def test_properties(self):
        micro_rna_gene_target = MicroRnaGeneTarget()
        micro_rna_gene_target.micro_rna_symbol='hsa-mir-3192'
        micro_rna_gene_target.id_entrez_genes=[1,2,3,4,5]

        self.assertEqual(micro_rna_gene_target.micro_rna_symbol, 'hsa-mir-3192')
        self.assertListEqual(micro_rna_gene_target.id_entrez_genes, [1, 2, 3, 4, 5])

    def test_equal(self):
        micro_rna_gene_target_list = [MicroRnaGeneTarget(micro_rna_symbol='hsa-mir-3192',
                                                         id_entrez_genes=[1,2,3,4,5]),
                                      MicroRnaGeneTarget(micro_rna_symbol='hsa-mir-312',
                                                         id_entrez_genes=[1, 2, 3, 4, 5]),
                                      MicroRnaGeneTarget(micro_rna_symbol='hsa-mir-3192',
                                                         id_entrez_genes=[1, 2, 3, 4, 5]),
                                      MicroRnaGeneTarget(micro_rna_symbol='hsa-mir-392',
                                                         id_entrez_genes=[1, 2, 3, 4, 5]),
                                      MicroRnaGeneTarget(micro_rna_symbol='hsa-mir-192',
                                                         id_entrez_genes=[1, 2, 3, 4, 5]),
                                      MicroRnaGeneTarget(micro_rna_symbol='hsa-mir-192',
                                                         id_entrez_genes=[1, 2, 3, 4, 5])]

        self.assertTrue(len(list(set(micro_rna_gene_target_list))), 3)

    def test_validation(self):
        micro_rna_gene_target = MicroRnaGeneTarget()
        micro_rna_gene_target.micro_rna_symbol = 'hsa-mir-3192'
        micro_rna_gene_target.id_entrez_genes = [1, 2, 3, 4, 5]

        try:
            micro_rna_gene_target.validate()
        except ValueError:
            self.fail('Encountered an unexpected exception.')

    def test_validation_fail(self):
        micro_rna_gene_target = MicroRnaGeneTarget(id_entrez_genes=[1,2,3,4,5])

        self.assertRaises(ValueError, micro_rna_gene_target.validate)

        micro_rna_gene_target = MicroRnaGeneTarget(micro_rna_symbol='hsa-mir-192')

        self.assertRaises(ValueError, micro_rna_gene_target.validate)

    def test_as_dict(self):
        micro_rna_gene_target = MicroRnaGeneTarget(micro_rna_symbol='hsa-mir-392',
                                                   id_entrez_genes=[1, 2, 3, 4, 5])

        micro_rna_gene_target_dict = micro_rna_gene_target.as_dict()

        self.assertTrue('micro_rna_symbol' in micro_rna_gene_target_dict)
        self.assertEqual(micro_rna_gene_target_dict['micro_rna_symbol'], 'hsa-mir-392')

        self.assertTrue('id_entrez_genes' in micro_rna_gene_target_dict)
        self.assertListEqual(micro_rna_gene_target_dict['id_entrez_genes'], [1, 2, 3, 4, 5])

if __name__ == '__main__':
    unittest.main()
