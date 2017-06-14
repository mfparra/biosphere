from Src.BioDataFileManagement.CrossCutting.Filters.FeSingleGeneAnnotationFile import FeSingleGeneAnnotationFile
from Src.BioDataFileManagement.Managers.GeneAnnotionFileManager import GeneAnnotationFileManager
from Src.BioDataImporter.Contracts.BioDataImporterBase import BioDataImporterBase
from Src.BioDataImporter.Entities.ImportationInfo import ImportationInfo
from Src.BioDataImporter.Entities.ImportationStatus import ImportationStatus
from Src.BioDataImporter.Mappers.Mapper import Mapper
from Src.BioDataManagement.CrossCutting.DTOs.GeneAnnotationDto import GeneAnnotationDto
from Src.BioDataManagement.Managers.GeneAnnotationManager import GeneAnnotationManager


class GeneAnnotationImporter(BioDataImporterBase):
    """
    This class is responsible for importing gene information.
    """
    def __init__(self):
        """"""
        self.__gene_file_manager = GeneAnnotationFileManager()
        self.__gene_manager = GeneAnnotationManager()


    def execute(self) -> ImportationInfo:
        """
        Execute the import data process for gene annotation.
        """
        importation_info = None

        try:
            fe_gene_file = self.__gene_file_manager.get(FeSingleGeneAnnotationFile(file='gene_annotation.txt'))
        except:
            importation_info = ImportationInfo(status=ImportationStatus.Fail,
                                               message='Gene Annotation Importation has failed. See details to more information.',
                                               details=['{0}. {1}'.format(ImportationStatus.Fail, 'Error in getting gene annotaion file.')])

        if importation_info:
            return importation_info

        gene_annotations = [Mapper.get_instance().map(g, GeneAnnotationDto) for g in fe_gene_file.result]

        try:
            self.__gene_manager.add_many(gene_annotations)
            importation_info = ImportationInfo(status=ImportationStatus.OK,
                                               message='Gene Annotation Importation has been successful. See details to more information.',
                                               details=['{0}. {1}'.format(ImportationStatus.OK.name,
                                                                          'Gene Annotation has saved in the system.')])
        except:
            importation_info = ImportationInfo(status=ImportationStatus.Fail,
                                               message='Gene Annotation Importation has failed. See details to more information.',
                                               details=['{0}. {1}'.format(ImportationStatus.Fail.name, 'Error in saving gene annotaion.')])
            
        return importation_info