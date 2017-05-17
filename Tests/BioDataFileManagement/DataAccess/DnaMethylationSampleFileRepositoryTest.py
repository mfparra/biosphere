import shutil
import tempfile
import unittest

from os import path

from Src.BioDataFileManagement.CrossCutting.Filters.FeListDnaMethylationSampleFile import FeListDnaMethylationSampleFile
from Src.BioDataFileManagement.DataAccess.DnaMethylationSampleFileRepository import DnaMethylationSampleFileRepository


class DnaMethylationSampleFileRepositoryTest(unittest.TestCase):
    def setUp(self):
        self.__repository_dir = tempfile.mkdtemp()
        self.__content = 'gene	normal	tumor\n' \
                         '1-Dec	0.8883	0.8047\n' \
                         '1-Mar	0.08760000000000001	0.3478\n' \
                         '1-Sep	0.08289999999999997	0.05780000000000002\n' \
                         '10-Mar	0.7335	0.8691\n' \
                         '11-Mar	0.02689999999999998	0.029799999999999993\n' \
                         '11-Sep	0.35235	0.42255\n' \
                         '13-Sep	0.23285	0.41225\n' \
                         '14-Sep	0.7915	0.8573999999999999\n' \
                         '3-Mar	0.12810000000000002	0.4094\n' \
                         '4-Mar	0.5357	0.13240000000000002\n' \
                         '5-Mar	0.26980000000000004	0.2691\n' \
                         '5-Sep	0.03689999999999999	0.10615000000000002\n' \
                         '6-Mar	0.055050000000000016	0.05965000000000001\n' \
                         '7-Mar	0.030100000000000016	0.031299999999999994\n' \
                         '8-Sep	0.91945	0.95765\n' \
                         '9-Mar	0.2904	0.4395\n' \
                         '9-Sep	0.22945000000000002	0.1565\n' \
                         'A1BG	0.458	0.8436\n' \
                         'A1CF	0.8236	0.32830000000000004\n' \
                         'A2BP1	0.59965	0.24280000000000002\n' \
                         'A2LD1	0.9491	0.8364\n' \
                         'A2M	0.8469	0.8831\n' \
                         'A2ML1	0.8938999999999999	0.9263'

    def tearDown(self):
        shutil.rmtree(self.__repository_dir)

    def test_get(self):
        with open(path.join(self.__repository_dir, 'dna_methylation.txt'), 'w') as file_temp:
            file_temp.write(self.__content)

        repository = DnaMethylationSampleFileRepository(self.__repository_dir)
        filter = repository.get(FeListDnaMethylationSampleFile())

        self.assertEqual(len(filter.result_list), 1)

        self.assertTrue(
            len([l for l in filter.result_list[0].dna_methylation_levels
                 if l.gene_symbol in ['1-Dec', '1-Mar', '1-Sep', '10-Mar', '11-Mar', '11-Sep', '13-Sep', '14-Sep', '3-Mar',
                                      '4-Mar', '5-Mar', '5-Sep', '6-Mar', '7-Mar', '8-Sep', '9-Mar', '9-Sep', 'A1BG', 'A1CF',
                                      'A2BP1', 'A2LD1', 'A2M', 'A2ML1']]), 23)


if __name__ == '__main__':
    unittest.main()
