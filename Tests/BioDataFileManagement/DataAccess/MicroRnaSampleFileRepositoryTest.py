import shutil
import tempfile
import unittest

from os import path, makedirs

from Src.BioDataFileManagement.CrossCutting.Filters.FeListMicroRnaSampleFile import FeListMicroRnaSampleFile
from Src.BioDataFileManagement.DataAccess.MicroRnaSampleFileRepository import MicroRnaSampleFileRepository


class MicroRnaSampleFileRepositoryTest(unittest.TestCase):
    def setUp(self):
        self.__repository_dir = tempfile.mkdtemp()
        self.__sub_directory = path.join(self.__repository_dir,'micro_rna_samples')

        if not path.exists( self.__sub_directory):
            makedirs(self.__sub_directory)

        self.__content = 'mirna	control	case\n' \
                         'hsa-mir-1322	0.0	0.0\n' \
                         'hsa-mir-1323	0.3028	0.0\n' \
                         'hsa-mir-3195	0.0	0.0\n' \
                         'hsa-mir-1321	0.0	0.0\n' \
                         'hsa-mir-3193	0.553	0.0\n' \
                         'hsa-mir-3192	0.0	0.0\n' \
                         'hsa-mir-1324	0.0	0.0\n' \
                         'hsa-mir-3190	0.0	0.0\n' \
                         'hsa-mir-675	4.6999	5.1553\n' \
                         'hsa-mir-676	0.7661	0.0\n' \
                         'hsa-mir-670	0.0	0.0\n' \
                         'hsa-mir-671	1.6332	3.9319\n' \
                         'hsa-mir-3198	0.0	1.0135\n' \
                         'hsa-mir-329-2	0.9518	0.0\n' \
                         'hsa-mir-3194	0.3028	0.0\n' \
                         'hsa-mir-770	0.553	0.0\n' \
                         'hsa-mir-7-2	0.0	1.6029\n' \
                         'hsa-mir-122	0.3028	0.0\n' \
                         'hsa-mir-219-1	0.9518	3.4838\n' \
                         'hsa-mir-3191	0.0	0.0\n'

    def tearDown(self):
        shutil.rmtree(self.__repository_dir)

    def test_get(self):
        with open(path.join(self.__sub_directory, 'micro_rna.txt'), 'w') as file_temp:
            file_temp.write(self.__content)

        repository = MicroRnaSampleFileRepository(self.__repository_dir)
        filter = repository.get(FeListMicroRnaSampleFile(sub_directory='micro_rna_samples'))

        self.assertEqual(len(filter.result_list), 1)

        self.assertTrue(
            len([l for l in filter.result_list[0].micro_rna_expression_levels
                 if l.symbol in ['hsa-mir-1322', 'hsa-mir-1323', 'hsa-mir-3195', 'hsa-mir-1321', 'hsa-mir-3193',
                                 'hsa-mir-3192', 'hsa-mir-1324', 'hsa-mir-3190', 'hsa-mir-675', 'hsa-mir-676',
                                 'hsa-mir-670', 'hsa-mir-671', 'hsa-mir-3198', 'hsa-mir-329-2', 'hsa-mir-3194',
                                 'hsa-mir-770', 'hsa-mir-7-2', 'hsa-mir-122', 'hsa-mir-219-1', 'hsa-mir-3191']]), 20)


if __name__ == '__main__':
    unittest.main()
