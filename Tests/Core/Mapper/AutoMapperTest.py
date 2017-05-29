import unittest

from Src.Core.Mapper.AutoMapper import AutoMapper
from Tests.Core.Mapper.FromTypeClass import FromTypeClass
from Tests.Core.Mapper.ToTypeClass import ToTypeClass


class AutoMapperTest(unittest.TestCase):

    def test_create_map_fail(self):
        auto_mapper = AutoMapper()
        auto_mapper.create_map(FromTypeClass, ToTypeClass)

        #self.assertRaises(Exception, GeneAnnotationFile)
        #self.assertRaises(Exception, GeneAnnotationFile, **{'symbol': 'abc', 'synonyms_genes': None})
        #self.assertRaises(Exception, GeneAnnotationFile, **{'id_entrez': 10, 'synonyms_genes': None})


if __name__ == '__main__':
    unittest.main()
