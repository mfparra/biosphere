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

    def test_read_all_files(self):
        for i in range(0, 10):
            tempfile.NamedTemporaryFile(dir=self.__repository_dir, suffix='.txt', delete=False)
            tempfile.NamedTemporaryFile(dir=self.__repository_dir, suffix='.gif', delete=False)

        files = FileUtils.read_all(self.__repository_dir, '\S+.*\.txt')

    def test_read_files_with_pagginate(self):
        for i in range(0, 10):
            tempfile.NamedTemporaryFile(dir=self.__repository_dir, suffix='.txt', delete=False)

        current_page = 0
        page_size = 3
        page_count = 0
        result_list_final = []

        current_page, \
        page_count, \
        result_list = FileUtils.read_with_pagginate(self.__repository_dir, page_size, current_page, page_count)

        result_list_final.extend(result_list)

        self.assertEqual(current_page, 1)
        self.assertEqual(page_count, 4)
        self.assertEqual(len(result_list), 3)

        current_page, \
        page_count, \
        result_list = FileUtils.read_with_pagginate(self.__repository_dir, page_size, current_page, page_count)

        result_list_final.extend(result_list)

        self.assertEqual(current_page, 2)
        self.assertEqual(page_count, 4)
        self.assertEqual(len(result_list), 3)

        current_page, \
        page_count, \
        result_list = FileUtils.read_with_pagginate(self.__repository_dir, page_size, current_page, page_count)

        result_list_final.extend(result_list)

        self.assertEqual(current_page, 3)
        self.assertEqual(page_count, 4)
        self.assertEqual(len(result_list), 3)

        current_page, \
        page_count, \
        result_list = FileUtils.read_with_pagginate(self.__repository_dir, page_size, current_page, page_count)

        result_list_final.extend(result_list)

        self.assertEqual(current_page, 4)
        self.assertEqual(page_count, 4)
        self.assertEqual(len(result_list), 1)
        self.assertEqual(len(result_list_final), 10)
        self.assertEqual(len(list(set(result_list_final))), 10)

    def test_get_files(self):
        for i in range(0, 10):
            tempfile.NamedTemporaryFile(dir=self.__repository_dir, suffix='.txt', delete=False)
            tempfile.NamedTemporaryFile(dir=self.__repository_dir, suffix='.gif', delete=False)

        self.assertEqual(len(FileUtils.get(self.__repository_dir, '\S+.*\.txt')), 10)


if __name__ == '__main__':
    unittest.main()
