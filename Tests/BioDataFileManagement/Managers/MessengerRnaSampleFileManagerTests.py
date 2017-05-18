import shutil
import tempfile
import unittest
from os import path

from Src.BioDataFileManagement.CrossCutting.Filters.FeListMessengerRnaSampleFile import FeListMessengerRnaSampleFile
from Src.BioDataFileManagement.Managers.MessengerRnaSampleFileManager import MessengerRnaSampleFileManager
from Tests.BioDataFileManagement.Managers.MessengerRnaSampleFileRepositoryMock import \
    MessengerRnaSampleFileRepositoryMock


class MessengerRnaSampleFileManagerTests(unittest.TestCase):
    def setUp(self):
        self.__repository_dir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.__repository_dir)

    def test_get(self):
        with open(path.join(self.__repository_dir, 'messenger_rna.txt'), 'w') as file_temp:
            file_temp.write('content')

        mock = MessengerRnaSampleFileRepositoryMock(self.__repository_dir)
        filter = FeListMessengerRnaSampleFile()
        manager = MessengerRnaSampleFileManager(mock)

        filter = manager.get(filter)

        self.assertTrue(len(filter.result_list) == 4)
        self.assertTrue(len([mrna.gene_expression_levels for mrna in filter.result_list
                             if len(mrna.gene_expression_levels) == 4]) == 4)


if __name__ == '__main__':
    unittest.main()
