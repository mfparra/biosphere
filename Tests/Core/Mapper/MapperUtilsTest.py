import unittest

from Src.Core.Mapper.MapperUtils import MapperUtils
from Tests.Core.Mapper.ToTypeClass import ToTypeClass


class MapperUtilsTest(unittest.TestCase):
    def test_get_properties_from_class(self):
        properties = MapperUtils.get_properties_from_class(ToTypeClass)
        self.assertListEqual(properties, ['id_entrez', 'symbol', 'synonyms_genes'])


if __name__ == '__main__':
    unittest.main()
