import unittest

from Src.BioDataFileManagement.CrossCutting.Entities.GeneAnnotation import GeneAnnotation
from Src.BioDataFileManagement.CrossCutting.Entities.MicroRnaGeneTarget import MicroRnaGeneTarget


class MicroRnaGeneTargetTest(unittest.TestCase):
    def test_instance(self):
        target = MicroRnaGeneTarget(microrna_symbol='hsa-miR-99b-5p',
                                    gene_target=GeneAnnotation(id_entrez=4942,
                                                               symbol='OAT'))

        self.assertEqual(target.microrna_symbol, 'HSA-MIR-99B-5P')
        self.assertEqual(target.gene_target.id_entrez, 4942)
        self.assertEqual(target.gene_target.symbol, 'OAT')
        self.assertEqual(target.gene_target.synonyms_genes, [])

    def test_instance_fail(self):
        self.assertRaises(ValueError, MicroRnaGeneTarget)
        self.assertRaises(ValueError, MicroRnaGeneTarget, **{'microrna_symbol': 'hsa-miR-99b-5p'})

    def test_equal(self):
        gene_annotations = [GeneAnnotation(id_entrez=10,
                                           symbol='abc',
                                           synonyms_genes=None),
                            GeneAnnotation(id_entrez=14,
                                           symbol='fha',
                                           synonyms_genes=['abd', 'rhj'])]

        targets = [MicroRnaGeneTarget(microrna_symbol='hsa-miR-99b-5p',
                                      gene_target=gene_annotations[0]),
                   MicroRnaGeneTarget(microrna_symbol='hsa-miR-6838-5p',
                                      gene_target=gene_annotations[1]),
                   MicroRnaGeneTarget(microrna_symbol='hsa-miR-99b-5p',
                                      gene_target=gene_annotations[0]),
                   MicroRnaGeneTarget(microrna_symbol='hsa-miR-6838-5p',
                                      gene_target=gene_annotations[1]),
                   MicroRnaGeneTarget(microrna_symbol='hsa-miR-93-5p',
                                      gene_target=gene_annotations[1])]

        self.assertEqual(len(list(set(targets))), 3)


if __name__ == '__main__':
    unittest.main()
