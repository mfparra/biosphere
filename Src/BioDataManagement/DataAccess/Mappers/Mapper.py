import threading

from mapper.object_mapper import ObjectMapper

from Src.BioDataManagement.CrossCutting.DTOs.GeneAnnotationDto import GeneAnnotationDto
from Src.BioDataManagement.DataAccess.Entities.GeneAnnotation import GeneAnnotation


class Mapper(object):
    __instance = None
    __lock = threading.Lock()

    def __init__(self):
        if (Mapper._instance != None):
            raise ('It is not allowed to create a class instance. Use MapperConfiguration.get_instance method.')

            Mapper._instance = self
        self.__configure()

    @staticmethod
    def get_instance():
        """
        
        :return: 
        """
        if Mapper.__instance is None:
            with Mapper._lock:
                if Mapper.__instance is None:
                    Mapper.__instance = Mapper()

        return Mapper.__instance

    def __configure(self):
        self.__mapper = ObjectMapper()
        self.__mapper.create_map(GeneAnnotationDto, GeneAnnotation)
        self.__mapper.create_map(GeneAnnotation, GeneAnnotationDto)

    def map(self, from_obj, to_type):
        """
        
        :param from_obj: 
        :param to_type: 
        :return: 
        """
        return self.__mapper.map(from_obj, to_type, ignore_case=True)


