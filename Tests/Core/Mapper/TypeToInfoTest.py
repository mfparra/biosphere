import unittest

from Src.BioDataFileManagement.CrossCutting.Entities.DnaMethylationLevel import DnaMethylationLevel
from Src.Core.Mapper.TypeToInfo import TypeToInfo
from Tests.Core.Mapper.ToTypeClass import ToTypeClass


class TypeToInfoTest(unittest.TestCase):
    def test_instance(self):
        type_to_info = TypeToInfo(class_type=ToTypeClass)

        self.assertEqual(type_to_info.class_type, ToTypeClass)
        self.assertListEqual(type_to_info.properties, ['id_entrez', 'symbol', 'synonyms_genes'])

    def test_instance_fail(self):
        self.assertRaises(ValueError, TypeToInfo)


if __name__ == '__main__':
    unittest.main()
