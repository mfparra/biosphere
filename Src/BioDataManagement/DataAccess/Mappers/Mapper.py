import threading

from Src.BioDataManagement.CrossCutting.DTOs.GeneAnnotationDto import GeneAnnotationDto
from Src.BioDataManagement.CrossCutting.DTOs.GeneExpressionLevelDto import GeneExpressionLevelDto
from Src.BioDataManagement.CrossCutting.DTOs.MessengerRnaSampleDto import MessengerRnaSampleDto
from Src.BioDataManagement.CrossCutting.DTOs.MicroRnaGeneTargetDto import MicroRnaGeneTargetDto
from Src.BioDataManagement.DataAccess.Entities.GeneAnnotation import GeneAnnotation
from Src.BioDataManagement.DataAccess.Entities.GeneExpressionLevel import GeneExpressionLevel
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

        return Mapper.__instance.__mapper

    def __configure(self):
        self.__mapper = AutoMapper()

        self.__gene_annotation_confiigure_map()
        self.__mirna_gene_target_configurate_map()
        self.__gene_expression_level_configure_map()
        self.__mran_sample_configure_map()

    def __gene_annotation_confiigure_map(self):
        self.__mapper.create_map(GeneAnnotationDto, GeneAnnotation)
        self.__mapper.create_map(GeneAnnotation, GeneAnnotationDto)

    def __mirna_gene_target_configurate_map(self):
        self.__mapper.create_map(MicroRnaGeneTargetDto, MicroRnaGeneTarget)
        self.__mapper.create_map(MicroRnaGeneTarget, MicroRnaGeneTargetDto)

    def __gene_expression_level_configure_map(self):
        self.__mapper.create_map(GeneExpressionLevelDto, GeneExpressionLevel, {'control': lambda dto: dto.control_value,
                                                                               'case': lambda dto: dto.case_value})
        self.__mapper.create_map(GeneExpressionLevel, GeneExpressionLevelDto,
                                 {'control_value': lambda entity: entity.control,
                                  'case_value': lambda entity: entity.case})

    def __mrna_sample_configure_map(self):
        self.__mapper.create_map(MessengerRnaSampleDto,
                                 MessengerRnaSample,
                                 {'exp_levels': lambda dto: [self.map(exp_dto, GeneExpressionLevel)
                                                             for exp_dto in dto.gene_expression_levels],
                                  })

        self.__mapper.create_map(MessengerRnaSample,
                                 MessengerRnaSampleDto,
                                 {'gene_expression_levels': lambda entity: [self.map(exp, GeneExpressionLevelDto)
                                                                            for exp in entity.exp_levels],
                                  })



