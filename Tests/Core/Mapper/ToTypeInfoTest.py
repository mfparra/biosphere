import unittest

from Src.BioDataFileManagement.CrossCutting.Entities.DnaMethylationLevel import DnaMethylationLevel
from Src.Core.Mapper.ToTypeInfo import ToTypeInfo
from Tests.Core.Mapper.ToTypeClass import ToTypeClass


class ToTypeInfoTest(unittest.TestCase):
    def test_instance(self):
        to_type_info = ToTypeInfo(class_type=ToTypeClass)

        self.assertEqual(to_type_info.class_type, ToTypeClass)
        self.assertListEqual(to_type_info.properties, ['id_entrez', 'symbol', 'synonyms_genes'])

    def test_instance_fail(self):
        self.assertRaises(ValueError, ToTypeInfo)


if __name__ == '__main__':
    unittest.main()
