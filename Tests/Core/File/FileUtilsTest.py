import shutil
import tempfile
import unittest

from os import path

from Src.Core.File.FileUtils import FileUtils


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.__repository_dir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.__repository_dir)

    def test_is_directory(self):
        self.assertTrue(FileUtils.is_directory(self.__repository_dir))

    def test_is_file(self):
        with open(path.join(self.__repository_dir, 'gene_annotation.txt'), 'w') as file_temp:
            file_temp.write('content')

        self.assertTrue(FileUtils.is_file(path.join(self.__repository_dir, 'gene_annotation.txt')))

    def test_read_file(self):
        with open(path.join(self.__repository_dir, 'gene_annotation.txt'), 'w') as file_temp:
            file_temp.write('content')

        self.assertEqual(FileUtils.read(path.join(self.__repository_dir, 'gene_annotation.txt')), 'content')


if __name__ == '__main__':
    unittest.main()
