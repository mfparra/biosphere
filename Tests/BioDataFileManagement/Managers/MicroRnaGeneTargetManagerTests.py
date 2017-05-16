import shutil
import tempfile
import unittest
from os import path

from Src.BioDataFileManagement.CrossCutting.Filters.FeSingleMicroRnaGeneTargetFile import FeSingleMicroRnaGeneTargetFile
from Src.BioDataFileManagement.Managers.MicroRnaGeneTargetFileManager import MicroRnaGeneTargetFileManager
from Tests.BioDataFileManagement.Managers.MicroRnaGeneTargetFileRepositoryMock import \
    MicroRnaGeneTargetFileRepositoryMock


class MicroRnaGeneTargetManagerTests(unittest.TestCase):
    def setUp(self):
        self.__repository_dir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.__repository_dir)

    def test_get(self):
        with open(path.join(self.__repository_dir, 'microrna_gene_target.txt'), 'w') as file_temp:
            file_temp.write('content')

        mock = MicroRnaGeneTargetFileRepositoryMock(self.__repository_dir)
        filter = FeSingleMicroRnaGeneTargetFile(file='microrna_gene_target.txt')
        manager = MicroRnaGeneTargetFileManager(mock)

        filter_result = manager.get(filter)

        self.assertTrue(len(filter_result.result) == 6)


if __name__ == '__main__':
    unittest.main()
