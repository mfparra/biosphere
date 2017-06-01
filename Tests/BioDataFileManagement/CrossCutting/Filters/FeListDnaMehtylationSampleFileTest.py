import unittest

from Src.BioDataFileManagement.CrossCutting.Filters.FeListDnaMethylationSampleFile import FeListDnaMethylationSampleFile


class FeListMessengerRnaSampleFileTest(unittest.TestCase):
    def test_instance(self):
        filter = FeListDnaMethylationSampleFile(pattern='\S+.*\.txt')

        self.assertEqual(filter.pattern, '\S+.*\.txt')
        self.assertEqual(filter.current_page, 0)
        self.assertEqual(filter.page_size, 10)
        self.assertEqual(filter.page_count, 0)
        self.assertTrue(filter.is_paged)
        self.assertListEqual(filter.result_list, [])
        self.assertEqual(filter.sub_directory, None)

        filter = FeListDnaMethylationSampleFile(pattern='\S+.*\.txt',
                                                current_page=1,
                                                page_size=20,
                                                page_count=13,
                                                is_paged=False,
                                                sub_directory='messenger_rna_samples')

        self.assertEqual(filter.current_page, 1)
        self.assertEqual(filter.page_size, 20)
        self.assertEqual(filter.page_count, 13)
        self.assertFalse(filter.is_paged)
        self.assertEqual(filter.sub_directory, 'messenger_rna_samples')

        filter.current_page = 2
        filter.page_size = 40
        filter.page_count = 7
        filter.is_paged = True
        filter.result_list =  ['BC', 'DF']

        self.assertEqual(filter.current_page, 2)
        self.assertEqual(filter.page_size, 40)
        self.assertEqual(filter.page_count, 7)
        self.assertTrue(filter.is_paged)
        self.assertListEqual(filter.result_list, ['BC', 'DF'])


if __name__ == '__main__':
    unittest.main()
