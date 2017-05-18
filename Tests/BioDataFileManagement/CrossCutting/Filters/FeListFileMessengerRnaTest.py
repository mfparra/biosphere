import unittest

from Src.BioDataFileManagement.CrossCutting.Filters.FeListMessengerRnaSampleFile import FeListMessengerRnaSampleFile


class FeListMessengerRnaSampleFileTests(unittest.TestCase):
    def test_instance(self):
        filter = FeListMessengerRnaSampleFile(pattern='\S+.*\.txt')

        self.assertEqual(filter.pattern, '\S+.*\.txt')
        self.assertEqual(filter.current_page, 0)
        self.assertEqual(filter.page_size, 10)
        self.assertEqual(filter.page_count, 0)
        self.assertTrue(filter.is_paged)
        self.assertListEqual(filter.result_list, [])

        filter = FeListMessengerRnaSampleFile(pattern='\S+.*\.txt',
                                              current_page=1,
                                              page_size=20,
                                              page_count=13,
                                              is_paged=False)

        self.assertEqual(filter.current_page, 1)
        self.assertEqual(filter.page_size, 20)
        self.assertEqual(filter.page_count, 13)
        self.assertFalse(filter.is_paged)

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
