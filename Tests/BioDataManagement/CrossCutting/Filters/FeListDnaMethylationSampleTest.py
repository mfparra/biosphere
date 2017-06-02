import unittest

from Src.BioDataManagement.CrossCutting.Filters.FeListDnaMethylationSample import FeListDnaMethylationSample


class FeListDnaMehylationSampleTest(unittest.TestCase):
    def test_instance(self):
        filter = FeListDnaMethylationSample(
            patient_id_list=['TCGA-A7-A0DB', 'TCGA-V7-A0DB', 'TCGA-A7-A1DB', 'TCGA-A7-A0DC'],
            dna_methylation_levels_from_patients={'TCGA-A7-A0DB':[1,2,3,4], 'TCGA-V7-A0DB':[1,2,3]})

        self.assertListEqual(filter.patient_id_list, ['TCGA-A7-A0DB', 'TCGA-V7-A0DB', 'TCGA-A7-A1DB', 'TCGA-A7-A0DC'])
        self.assertListEqual(filter.dna_methylation_levels_from_patients['TCGA-A7-A0DB'], [1,2,3,4])
        self.assertListEqual(filter.dna_methylation_levels_from_patients['TCGA-V7-A0DB'], [1,2,3])


if __name__ == '__main__':
    unittest.main()
