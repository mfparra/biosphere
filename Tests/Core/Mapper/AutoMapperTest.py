import unittest

from Src.Core.Mapper.AutoMapper import AutoMapper
from Tests.Core.Mapper.FromTypeClass import FromTypeClass
from Tests.Core.Mapper.ToTypeClass import ToTypeClass


class AutoMapperTest(unittest.TestCase):

    def test_create_map_fail(self):
        auto_mapper = AutoMapper()
        auto_mapper.create_map(FromTypeClass, ToTypeClass)

        self.assertRaises(ValueError, auto_mapper.create_map, **{'from_type': None, 'to_type': ToTypeClass})
        self.assertRaises(ValueError, auto_mapper.create_map, **{'from_type': FromTypeClass, 'to_type': None})

    def test_map(self):
        auto_mapper = AutoMapper()
        auto_mapper.create_map(FromTypeClass, ToTypeClass)

        from_obj = FromTypeClass()
        to_obj = auto_mapper.map(from_obj, ToTypeClass)

        self.assertEqual(from_obj.id_entrez, to_obj.id_entrez)
        self.assertEqual(from_obj.symbol, to_obj.symbol)
        self.assertEqual(from_obj.synonyms_genes, to_obj.synonyms_genes)

        from_obj = FromTypeClass(id_entrez=1,
                                 symbol='ABC',
                                 synonyms_genes=['ABC', 'HC1', 'UQ2'])
        to_obj = auto_mapper.map(from_obj, ToTypeClass)

        self.assertEqual(from_obj.id_entrez, to_obj.id_entrez)
        self.assertEqual(from_obj.symbol, to_obj.symbol)
        self.assertEqual(from_obj.synonyms_genes, to_obj.synonyms_genes)

    def test_map_fail(self):
        auto_mapper = AutoMapper()
        auto_mapper.create_map(FromTypeClass, ToTypeClass)

        self.assertRaises(ValueError, auto_mapper.map, **{'from_obj': None, 'to_type': ToTypeClass})
        self.assertRaises(ValueError, auto_mapper.map, **{'from_obj': FromTypeClass(), 'to_type': None})
        self.assertRaises(Exception, auto_mapper.map, **{'from_obj': ToTypeClass(), 'to_type': FromTypeClass})

if __name__ == '__main__':
    unittest.main()
