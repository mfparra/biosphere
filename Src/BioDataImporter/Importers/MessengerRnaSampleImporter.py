from Src.BioDataFileManagement.CrossCutting.Filters.FeListMessengerRnaSampleFile import FeListMessengerRnaSampleFile
from Src.BioDataFileManagement.Managers.MessengerRnaSampleFileManager import MessengerRnaSampleFileManager
from Src.BioDataImporter.Contracts.BioDataImporterBase import BioDataImporterBase
from Src.BioDataImporter.Entities.ImportationInfo import ImportationInfo
from Src.BioDataImporter.Entities.ImportationStatus import ImportationStatus
from Src.BioDataImporter.Mappers import Mapper
from Src.BioDataManagement.CrossCutting.DTOs.MessengerRnaSampleDto import MessengerRnaSampleDto
from Src.BioDataManagement.Managers.MessengerRnaSampleManager import MessengerRnaSampleManager


class MessengerRnaSampleImporter(BioDataImporterBase):
    """
    This class is responsible for importing Messenger RNA samples.
    """
    def __init__(self):
        self.__mrna_sample_file_manager = MessengerRnaSampleFileManager()
        self.__mrna_sample_manager = MessengerRnaSampleManager()

    def execute(self):
        """
        Execute the import data process for messenger RNA sampples.
        """
        importation_info = None

        try:
            fe_mrna_sample_file = self.__mrna_sample_file_manager.get(FeListMessengerRnaSampleFile())
        except:
            importation_info = ImportationInfo(status=ImportationStatus.Fail,
                                               message='Messenger RNA Sample Importation has failed. See details to more information.',
                                               details=['{0}. {1}'.format(ImportationStatus.Fail,
                                                                          'Error in getting Messenger RNA Sample files.')])

        if importation_info:
            return importation_info


        mrna_samples = [Mapper.get_instance().map(sample, MessengerRnaSampleDto) for sample in fe_mrna_sample_file.result]

        try:
            self.__mrna_sample_manager.add_many(mrna_samples)
            importation_info = ImportationInfo(status=ImportationStatus.OK,
                                               message='Messenger RNA Sample Importation has been successful. See details to more information.',
                                               details=['{0}. {1}'.format(ImportationStatus.OK,
                                                                          'Messenger RNA Samples have saved in the system.')])
        except:
            importation_info = ImportationInfo(status=ImportationStatus.Fail,
                                               message='Gene Annotation Importation has failed. See details to more information.',
                                               details=['{0}. {1}'.format(ImportationStatus.Fail,
                                                                          'Error in saving Messenger RNA Samples.')])

        return importation_info