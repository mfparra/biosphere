import unittest

from Src.BioDataManagement.CrossCutting.DTOs.MicroRnaGeneTargetDto import MicroRnaGeneTargetDto


class MicroRnaGeneTargetDtoTest(unittest.TestCase):
    def test_instance(self):
        micro_rna_gene_target_dto = MicroRnaGeneTargetDto(micro_rna_symbol='hsa-mir-3192',
                                                          id_entrez_genes=[1,2,3,4,5,6])

        self.assertEqual(micro_rna_gene_target_dto.micro_rna_symbol, 'hsa-mir-3192')
        self.assertListEqual(micro_rna_gene_target_dto.id_entrez_genes, [1,2,3,4,5,6])

    def test_properties(self):
        micro_rna_gene_target_dto = MicroRnaGeneTargetDto()
        micro_rna_gene_target_dto.micro_rna_symbol='hsa-mir-3192'
        micro_rna_gene_target_dto.id_entrez_genes=[1,2,3,4,5,6]

        self.assertEqual(micro_rna_gene_target_dto.micro_rna_symbol, 'hsa-mir-3192')
        self.assertListEqual(micro_rna_gene_target_dto.id_entrez_genes, [1, 2, 3, 4, 5, 6])

    def test_equal(self):
        micro_rna_gene_target_dto = [MicroRnaGeneTargetDto(micro_rna_symbol='hsa-mir-3192',
                                                          id_entrez_genes=[1,2,3,4,5,6]),
                                     MicroRnaGeneTargetDto(micro_rna_symbol='hsa-mir-3191',
                                                           id_entrez_genes=[1, 2, 3, 4, 5, 6]),
                                     MicroRnaGeneTargetDto(micro_rna_symbol='hsa-mir-3192',
                                                           id_entrez_genes=[1, 2, 3, 4, 5, 6]),
                                     MicroRnaGeneTargetDto(micro_rna_symbol='hsa-mir-2192',
                                                           id_entrez_genes=[1, 2, 3, 4, 5, 6]),
                                     MicroRnaGeneTargetDto(micro_rna_symbol='hsa-mir-3092',
                                                           id_entrez_genes=[1, 2, 3, 4, 5, 6])]

        self.assertTrue(len(list(set(micro_rna_gene_target_dto))) == 4)

if __name__ == '__main__':
    unittest.main()
