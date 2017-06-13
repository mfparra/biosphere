from Src.BioDataFileManagement.CrossCutting.Filters.FeSingleMicroRnaGeneTargetFile import FeSingleMicroRnaGeneTargetFile
from Src.BioDataFileManagement.Managers.MicroRnaGeneTargetFileManager import MicroRnaGeneTargetFileManager
from Src.BioDataImporter.Contracts.BioDataImporterBase import BioDataImporterBase
from Src.BioDataImporter.Entities.ImportationInfo import ImportationInfo
from Src.BioDataImporter.Entities.ImportationStatus import ImportationStatus
from Src.BioDataImporter.Mappers.Mapper import Mapper
from Src.BioDataManagement.CrossCutting.DTOs.MicroRnaGeneTargetDto import MicroRnaGeneTargetDto
from Src.BioDataManagement.Managers.MicroRnaGeneTargetManager import MicroRnaGeneTargetManager


class MicroRnaGeneTargetImporter(BioDataImporterBase):
    """
    This class is responsible for importing microRna gene target information.
    """
    def __init__(self):
        """"""
        self.__target_file_manager = MicroRnaGeneTargetFileManager()
        self.__target_manager = MicroRnaGeneTargetManager()


    def execute(self):
        """
        Execute the import data process for microRNA annotation.
        """
        importation_info = None

        try:
            fe_target_file = self._target_file_manager.get(FeSingleMicroRnaGeneTargetFile())
        except:
            importation_info = ImportationInfo(status=ImportationStatus.Fail,
                                               message='MicroRNA Gene Target Importation has failed. See details to more information.',
                                               details=['{0}. {1}'.format(ImportationStatus.Fail,
                                                                          'Error in getting microRNA gene target file.')])

        if importation_info:
            return importation_info

        targets = self.__get_targets_dto(fe_target_file.result)

        try:
            self.__target_manager.add_many(targets)
            importation_info = ImportationInfo(status=ImportationStatus.OK,
                                               message='MicroRNA Gene Target Importation has been successful. See details to more information.',
                                               details=['{0}. {1}'.format(ImportationStatus.OK,
                                                                          'MicroRNA Gene Target has saved in the system.')])
        except:
            importation_info = ImportationInfo(status=ImportationStatus.Fail,
                                               message='MicroRNA Gene Target Importation has failed. See details to more information.',
                                               details=['{0}. {1}'.format(ImportationStatus.Fail,
                                                                          'Error in saving microRNA Gene Targets.')])

        return importation_info

    def __get_targets_dto(self, target_file_list):
        mirnas = list(set(map(lambda t: t.micro_rna_symbol, target_file_list)))
        target_file = map(lambda m: (m, list(filter(lambda t: m == t.micro_rna_symbol, target_file_list))),
                          mirnas)

        return map(lambda t: Mapper.get_instance().map(t, MicroRnaGeneTargetDto, 'micro_rna_gene_targets'), target_file)