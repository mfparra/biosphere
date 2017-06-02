import os

from pymongo import MongoClient
from yaak import inject

from Src.BioDataFileManagement.DataAccess.GeneAnnotationFileRepository import GeneAnnotationFileRepository
from Src.BioDataFileManagement.DataAccess.MessengerRnaSampleFileRepository import MessengerRnaSampleFileRepository
from Src.BioDataFileManagement.DataAccess.MicroRnaGeneTargetFileRepository import MicroRnaGeneTargetFileRepository
from Src.BioDataFileManagement.DataAccess.MicroRnaSampleFileRepository import MicroRnaSampleFileRepository
from Src.BioDataManagement.DataAccess.Repositories.DnaMethylationSampleRepository import DnaMethylationSampleRepository
from Src.BioDataManagement.DataAccess.Repositories.GeneAnnotionRepository import GeneAnnotationRepository
from Src.BioDataManagement.DataAccess.Repositories.MessengerRnaSampleRepository import MessengerRnaSampleRepository
from Src.BioDataManagement.DataAccess.Repositories.MicroRnaGeneTargetRepository import MicroRnaGeneTargetRepository


class ApplicationContainer(object):
    """description of class"""

    def __init__(self):
        """description of initialize"""

        # windows
        self.__file_base_directory = 'C:\\Users\\Carlos\\Documents\\dados_teste'
        self.__gene_annotaion_file_directory = os.path.join(self.__file_base_directory, 'system\gene')
        self.__mirna_gene_targets_file_directory = os.path.join(self.__file_base_directory, 'system\gmirna_gene_targets')

        self.__set_providers()

    def __set_providers(self):
        """description of method"""

        self.__set_bio_data_file_providers()
        self.__set_bio_data_providers()

    def __set_bio_data_file_providers(self):
        inject.provide('GeneAnnotationFileRepositoryBase',
                       lambda: GeneAnnotationFileRepository(self.__gene_annotaion_file_directory),
                       scope=inject.Scope.Application)
        inject.provide('MicroRnaGeneTargetFileRepositoryBase', lambda: MicroRnaGeneTargetFileRepository(self.__mirna_gene_targets_file_directory),
                       scope=inject.Scope.Application)

        inject.provide('MessengerRnaFileRepositoryBase', lambda: MessengerRnaSampleFileRepository(self.__file_base_directory),
                       scope=inject.Scope.Application)
        inject.provide('MicroRnaFileRepositoryBase', lambda: MicroRnaSampleFileRepository(self.__file_base_directory),
                       scope=inject.Scope.Application)

    def __set_bio_data_providers(self):
        client = MongoClient('localhost', 27017)
        db = client.biosphere_db

        inject.provide('GeneAnnotationRepositoryBase', lambda: GeneAnnotationRepository(db), scope=inject.Scope.Application)
        inject.provide('DnaMethylationRepositoryBase', lambda: MicroRnaGeneTargetRepository(db),
                       scope=inject.Scope.Application)
        inject.provide('MessengerRnaSampleRepositoryBase', lambda: MessengerRnaSampleRepository(db),
                       scope=inject.Scope.Application)
        inject.provide('DnaMethylationSampleRepositoryBase', lambda: DnaMethylationSampleRepository(db),
                       scope=inject.Scope.Application)

        #inject.provide('GeneSelectedRepositoryBase', lambda: gene_selected_repository, scope=inject.Scope.Application)
        #inject.provide('NetworkRepositoryBase', lambda: network_repository, scope=inject.Scope.Application)

    def __del__(self):
        """description of method"""
        inject.clear()