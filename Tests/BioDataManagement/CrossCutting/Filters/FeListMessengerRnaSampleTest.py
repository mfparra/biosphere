import unittest

from Src.BioDataManagement.CrossCutting.Filters.FeListMessengerRnaSample import FeListMessengerRnaSample


class FeListMessengerRnaSampleTest(unittest.TestCase):
    def test_instance(self):
        filter = FeListMessengerRnaSample(
            patient_id_list=['TCGA-A7-A0DB', 'TCGA-V7-A0DB', 'TCGA-A7-A1DB', 'TCGA-A7-A0DC'],
            gene_expression_levels_from_patients={'TCGA-A7-A0DB':[1,2,3,4], 'TCGA-V7-A0DB':[1,2,3]})

        self.assertListEqual(filter.patient_id_list, ['TCGA-A7-A0DB', 'TCGA-V7-A0DB', 'TCGA-A7-A1DB', 'TCGA-A7-A0DC'])
        self.assertListEqual(filter.gene_expression_levels_from_patients['TCGA-A7-A0DB'], [1,2,3,4])
        self.assertListEqual(filter.gene_expression_levels_from_patients['TCGA-V7-A0DB'], [1,2,3])


if __name__ == '__main__':
    unittest.main()
