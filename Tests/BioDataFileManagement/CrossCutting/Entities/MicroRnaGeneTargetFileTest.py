import unittest

from Src.BioDataFileManagement.CrossCutting.Entities.GeneAnnotationFile import GeneAnnotationFile
from Src.BioDataFileManagement.CrossCutting.Entities.MicroRnaGeneTargetFile import MicroRnaGeneTargetFile


class MicroRnaGeneTargetTest(unittest.TestCase):
    def test_instance(self):
        target = MicroRnaGeneTargetFile(microrna_symbol='hsa-miR-99b-5p',
                                        gene_target=GeneAnnotationFile(id_entrez=4942,
                                                                       symbol='OAT'))

        self.assertEqual(target.microrna_symbol, 'HSA-MIR-99B-5P')
        self.assertEqual(target.gene_target.id_entrez, 4942)
        self.assertEqual(target.gene_target.symbol, 'OAT')
        self.assertEqual(target.gene_target.synonyms_genes, [])

    def test_instance_fail(self):
        self.assertRaises(ValueError, MicroRnaGeneTargetFile)
        self.assertRaises(ValueError, MicroRnaGeneTargetFile, **{'microrna_symbol': 'hsa-miR-99b-5p'})

    def test_equal(self):
        gene_annotations = [GeneAnnotationFile(id_entrez=10,
                                               symbol='abc',
                                               synonyms_genes=None),
                            GeneAnnotationFile(id_entrez=14,
                                               symbol='fha',
                                               synonyms_genes=['abd', 'rhj'])]

        targets = [MicroRnaGeneTargetFile(microrna_symbol='hsa-miR-99b-5p',
                                          gene_target=gene_annotations[0]),
                   MicroRnaGeneTargetFile(microrna_symbol='hsa-miR-6838-5p',
                                          gene_target=gene_annotations[1]),
                   MicroRnaGeneTargetFile(microrna_symbol='hsa-miR-99b-5p',
                                          gene_target=gene_annotations[0]),
                   MicroRnaGeneTargetFile(microrna_symbol='hsa-miR-6838-5p',
                                          gene_target=gene_annotations[1]),
                   MicroRnaGeneTargetFile(microrna_symbol='hsa-miR-93-5p',
                                          gene_target=gene_annotations[1])]

        self.assertEqual(len(list(set(targets))), 3)


if __name__ == '__main__':
    unittest.main()
