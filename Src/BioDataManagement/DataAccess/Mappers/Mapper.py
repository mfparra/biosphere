import threading

from Src.BioDataManagement.CrossCutting.DTOs.GeneAnnotationDto import GeneAnnotationDto
from Src.BioDataManagement.CrossCutting.DTOs.MessengerRnaSampleDto import MessengerRnaSampleDto
from Src.BioDataManagement.CrossCutting.DTOs.MicroRnaGeneTargetDto import MicroRnaGeneTargetDto
from Src.BioDataManagement.DataAccess.Entities.GeneAnnotation import GeneAnnotation
from Src.BioDataManagement.DataAccess.Entities.MessengerRnaSample import MessengerRnaSample
from Src.BioDataManagement.DataAccess.Entities.MicroRnaGeneTarget import MicroRnaGeneTarget
from Src.Core.Mapper.AutoMapper import AutoMapper


class Mapper(object):
    __instance = None
    __lock = threading.Lock()

    def __init__(self):
        if (Mapper.__instance != None):
            raise ('It is not allowed to create a class instance. Use Mapper.get_instance method.')

            Mapper.__instance = self

        self.__mapper = None
        self.__configure()

    @staticmethod
    def get_instance():
        """
        
        :return: 
        """
        if Mapper.__instance is None:
            with Mapper.__lock:
                if Mapper.__instance is None:
                    Mapper.__instance = Mapper()

        return Mapper.__instance

    def __configure(self):
        self.__mapper = AutoMapper()

        self.__mapper.create_map(GeneAnnotationDto, GeneAnnotation)
        self.__mapper.create_map(GeneAnnotation, GeneAnnotationDto)

        self.__mapper.create_map(MicroRnaGeneTargetDto, MicroRnaGeneTarget)
        self.__mapper.create_map(MicroRnaGeneTarget, MicroRnaGeneTargetDto)

        self.__mapper.create_map(MessengerRnaSampleDto, MessengerRnaSample)
        self.__mapper.create_map(MessengerRnaSample, MessengerRnaSampleDto)

    def map(self, from_obj, to_type, ignore_case=True):
        """
        
        :param from_obj: 
        :param to_type: 
        :return: 
        """
        return self.__mapper.map(from_obj, to_type, ignore_case)




