import shutil
import tempfile
import unittest
from os import path

from Src.BioDataFileManagement.CrossCutting.Filters.FeListDnaMethylationSampleFile import FeListDnaMethylationSampleFile
from Src.BioDataFileManagement.Managers.DnaMethylationSampleFileManager import DnaMethylationSampleFileManager
from Tests.BioDataFileManagement.Managers.DnaMethylationSampleFileRepositoryMock import \
    DnaMethylationSampleFileRepositoryMock


class DnaMethylationSampleFileManagerTests(unittest.TestCase):
    def setUp(self):
        self.__repository_dir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.__repository_dir)

    def test_get(self):
        with open(path.join(self.__repository_dir, 'dna_methylation.txt'), 'w') as file_temp:
            file_temp.write('content')

        mock = DnaMethylationSampleFileRepositoryMock(self.__repository_dir)
        filter = FeListDnaMethylationSampleFile()
        manager = DnaMethylationSampleFileManager(mock)

        filter = manager.get(filter)

        self.assertTrue(len(filter.result_list) == 4)
        self.assertTrue(len([dm.dna_methylation_levels for dm in filter.result_list
                             if len(dm.dna_methylation_levels) == 4]) == 4)


if __name__ == '__main__':
    unittest.main()
