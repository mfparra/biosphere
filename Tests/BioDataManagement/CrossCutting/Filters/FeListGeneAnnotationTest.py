import unittest

from Src.BioDataManagement.CrossCutting.Filters.FeListGeneAnnotation import FeListGeneAnnotation


class FeListGeneAnnotationTest(unittest.TestCase):
    def test_instance(self):
        filter = FeListGeneAnnotation(id_entrez_list=[1,2,3,4,5])

        self.assertListEqual(filter.id_entrez_list, [1,2,3,4,5])



if __name__ == '__main__':
    unittest.main()
