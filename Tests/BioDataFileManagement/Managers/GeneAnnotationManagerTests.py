import shutil
import tempfile
import unittest
from os import path

from Src.BioDataFileManagement.CrossCutting.Filters.FeSingleGeneAnnotationFile import FeSingleGeneAnnotationFile
from Src.BioDataFileManagement.Managers.GeneAnnotionFileManager import GeneAnnotationFileManager
from Tests.BioDataFileManagement.Managers.GeneAnnotationFileRepositoryMock import GeneAnnotaionFileRepositoryMock


class GeneAnnotationManagerTests(unittest.TestCase):
    def setUp(self):
        self.__repository_dir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.__repository_dir)

    def test_get(self):
        with open(path.join(self.__repository_dir, 'gene_annotation.txt'), 'w') as file_temp:
            file_temp.write('content')

        mock = GeneAnnotaionFileRepositoryMock(self.__repository_dir)
        filter = FeSingleGeneAnnotationFile(file='gene_annotation.txt')
        manager = GeneAnnotationFileManager(mock)

        filter_result = manager.get(filter)

        self.assertTrue(len(filter_result.result) == 4)
        self.assertTrue(len([ga.synonyms_genes for ga in filter_result.result if ga.synonyms_genes]) == 2)


if __name__ == '__main__':
    unittest.main()
