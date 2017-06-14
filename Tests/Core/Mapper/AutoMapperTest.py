import unittest

from Src.Core.Mapper.AutoMapper import AutoMapper
from Tests.Core.Mapper.ToTypeClass2 import ToTypeClass2
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

    def test_map_with_mapping(self):
        auto_mapper = AutoMapper()
        auto_mapper.create_map(FromTypeClass, ToTypeClass2, {'id': lambda x: x.id_entrez,
                                                             'synonyms': lambda x: x.synonyms_genes,
                                                             'locus': lambda x: None})

        from_obj = FromTypeClass(id_entrez=1,
                                 symbol='ABC',
                                 synonyms_genes=['ABC', 'HC1', 'UQ2'])

        to_obj = auto_mapper.map(from_obj, ToTypeClass2)

        self.assertEqual(from_obj.id_entrez, to_obj.id)
        self.assertEqual(from_obj.symbol, to_obj.symbol)
        self.assertEqual(from_obj.synonyms_genes, to_obj.synonyms)
        self.assertIsNone(to_obj.locus)

    def test_map_with_from_type_class_str_and_mapping(self):
        auto_mapper = AutoMapper()
        auto_mapper.create_map('FromTypeClass', ToTypeClass2, {'id': lambda x: x['id'],
                                                               'synonyms': lambda x: x['synonyms'],
                                                               'symbol': lambda x: x['symbol'],
                                                               'locus': lambda x: None})

        from_obj = {'id':10, 'synonyms': [1,2,3,4], 'symbol':'AD1'}
        to_obj = auto_mapper.map(from_obj, ToTypeClass2, from_obj_class_name='FromTypeClass')

        self.assertEqual(to_obj.id, from_obj['id'])
        self.assertEqual(to_obj.symbol, from_obj['symbol'])
        self.assertEqual(to_obj.synonyms, from_obj['synonyms'])
        self.assertIsNone(to_obj.locus)

    def test_map_fail(self):
        auto_mapper = AutoMapper()
        auto_mapper.create_map(FromTypeClass, ToTypeClass)

        self.assertRaises(ValueError, auto_mapper.map, **{'from_obj': None, 'to_type': ToTypeClass})
        self.assertRaises(ValueError, auto_mapper.map, **{'from_obj': FromTypeClass(), 'to_type': None})
        self.assertRaises(Exception, auto_mapper.map, **{'from_obj': ToTypeClass(), 'to_type': FromTypeClass})

if __name__ == '__main__':
    unittest.main()
