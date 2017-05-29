import threading

from Src.BioDataManagement.CrossCutting.DTOs.GeneAnnotationDto import GeneAnnotationDto
from Src.BioDataManagement.DataAccess.Entities.GeneAnnotation import GeneAnnotation


class Mapper(object):
    __instance = None
    __lock = threading.Lock()

    def __init__(self):
        if (Mapper.__instance != None):
            raise ('It is not allowed to create a class instance. Use MapperConfiguration.get_instance method.')

            Mapper._instance = self
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
        self.__create_map(GeneAnnotationDto, GeneAnnotation, {'id_entrez': lambda g : g.id_entrez})
        self.__create_map(GeneAnnotation, GeneAnnotationDto)

    def map(self, from_obj, to_type):
        """
        
        :param from_obj: 
        :param to_type: 
        :return: 
        """
        return self.__mapper.map(from_obj, to_type, ignore_case=True)

    def __create_map(self, type_from, type_to, mapping=None):
        property_names = [p for p in dir(type_to) if isinstance(getattr(type_to, p), property)]
        print('')


