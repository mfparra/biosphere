import unittest
from unittest.mock import Mock, patch

from yaak import inject

from Src.BioDataFileManagement.CrossCutting.Contracts.GeneAnnotationFileRepositoryBase import \
    GeneAnnotationFileRepositoryBase
from Src.BioDataFileManagement.CrossCutting.Entities.GeneAnnotationFile import GeneAnnotationFile
from Src.BioDataFileManagement.CrossCutting.Filters.FeSingleGeneAnnotationFile import FeSingleGeneAnnotationFile
from Src.BioDataImporter.Entities.ImportationStatus import ImportationStatus
from Src.BioDataImporter.Importers.GeneAnnotationImporter import GeneAnnotationImporter
from Src.BioDataManagement.CrossCutting.Contracts.GeneAnnotationRepositoryBase import GeneAnnotationRepositoryBase
from Src.BioDataManagement.CrossCutting.DTOs.GeneAnnotationDto import GeneAnnotationDto
from Src.BioDataManagement.CrossCutting.Filters.FeListGeneAnnotation import FeListGeneAnnotation


class GeneAnnotationImporterTest(unittest.TestCase):
    def setUp(self):
        self.__configure_file_repository()
        self.__configure_repository()

        inject.provide('GeneAnnotationFileRepositoryBase', self.__file_repository, scope=inject.Scope.Application)
        inject.provide('GeneAnnotationRepositoryBase', self.__repository, scope=inject.Scope.Application)

    def tearDown(self):
        inject.clear()

    def __configure_file_repository(self):
        fe = FeSingleGeneAnnotationFile(file='gene_annotation.txt')
        fe.result = [GeneAnnotationFile(id_entrez=12, symbol='A2MP1',
                                        synonyms_genes=['A2MD', 'CPAMD5', 'FWP007', 'S863-7']),
                     GeneAnnotationFile(id_entrez=121, symbol='ACACB',
                                        synonyms_genes=['HEL70']),
                     GeneAnnotationFile(id_entrez=1, symbol='RPS10-NUDT3',
                                        synonyms_genes=['-']),
                     GeneAnnotationFile(id_entrez=89, symbol='AANAT',
                                        synonyms_genes=['-'])]

        self.__file_repository = Mock(spec=GeneAnnotationFileRepositoryBase)
        self.__file_repository.get.return_value = fe

    def __configure_repository(self):
        self.__repository = Mock(spec=GeneAnnotationRepositoryBase)
        self.__repository.get_many.return_value =  FeListGeneAnnotation()

    def test_execute(self):
        importer = GeneAnnotationImporter()
        importation_info = importer.execute()

        self.assertEqual(importation_info.status, ImportationStatus.OK)
        self.assertEqual(importation_info.message, 'Gene Annotation Importation has been successful. See details to more information.')
        self.assertListEqual(importation_info.details, ['OK. Gene Annotation has saved in the system.'])

        with patch.object(self.__file_repository, 'get') as mock:
            importer.execute()
            mock.assert_called_with([GeneAnnotationFile(id_entrez=12, symbol='A2MP1',
                                                        synonyms_genes=['A2MD', 'CPAMD5', 'FWP007', 'S863-7']),
                                     GeneAnnotationFile(id_entrez=121, symbol='ACACB',
                                                        synonyms_genes=['HEL70']),
                                     GeneAnnotationFile(id_entrez=1, symbol='RPS10-NUDT3',
                                                        synonyms_genes=['-']),
                                     GeneAnnotationFile(id_entrez=89, symbol='AANAT',
                                                        synonyms_genes=['-'])])

        with patch.object(self.__repository, 'add_many') as mock:
            importer.execute()
            mock.assert_called_with([GeneAnnotationDto(id_entrez=12, symbol='A2MP1', synonyms_genes=['A2MD', 'CPAMD5', 'FWP007', 'S863-7']),
                                     GeneAnnotationDto(id_entrez=121, symbol='ACACB', synonyms_genes=['HEL70']),
                                     GeneAnnotationDto(id_entrez=1, symbol='RPS10-NUDT3', synonyms_genes=['-']),
                                     GeneAnnotationDto(id_entrez=89, symbol='AANAT', synonyms_genes=['-'])])

        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
