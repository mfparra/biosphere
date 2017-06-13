import threading

from Src.BioDataFileManagement.CrossCutting import Entities
from Src.BioDataFileManagement.CrossCutting.Entities.GeneAnnotationFile import GeneAnnotationFile
from Src.BioDataFileManagement.CrossCutting.Entities.MessengerRnaSampleFile import MessengerRnaSampleFile
from Src.BioDataManagement.CrossCutting.DTOs.GeneAnnotationDto import GeneAnnotationDto
from Src.BioDataManagement.CrossCutting.DTOs.GeneExpressionLevelDto import GeneExpressionLevelDto
from Src.BioDataManagement.CrossCutting.DTOs.MessengerRnaSampleDto import MessengerRnaSampleDto
from Src.BioDataManagement.CrossCutting.DTOs.MicroRnaGeneTargetDto import MicroRnaGeneTargetDto
from Src.BioDataManagement.CrossCutting.Filters.FeListGeneAnnotation import FeListGeneAnnotation
from Src.BioDataManagement.Managers.GeneAnnotationManager import GeneAnnotationManager
from Src.Core.Mapper.AutoMapper import AutoMapper


class Mapper(object):
    __instance = None
    __lock = threading.Lock()

    def __init__(self):
        if (Mapper.__instance != None):
            raise ('It is not allowed to create a class instance. Use Mapper.get_instance method.')

            Mapper.__instance = self

        self.__mapper = None
        self.__gene_annotations = self.__get_gene_annotations()
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

        self.__mapper.create_map(GeneAnnotationFile, GeneAnnotationDto, {'synonyms': lambda g: g.synonyms_genes})

        self.__mapper.create_map('micro_rna_gene_targets',
                                 MicroRnaGeneTargetDto,
                                 {'micro_rna_symbol': lambda m: m[0],
                                  'id_entrez_genes': self.__id_entrez_gene(map(lambda g: self.__get_gene_annotations(g.gene_symbol)))})

        self.__mapper.create_map(Entities.GeneExpressionLevel,
                                 GeneExpressionLevelDto,
                                 {'id_entrez': lambda g: self.__id_entrez_gene(self.__get_id_entrez_gene(g.gene_symbol))})

        self.__mapper.create_map(MessengerRnaSampleFile,
                                 MessengerRnaSampleDto,
                                 {'gene_expression_levels': lambda entity: [self.map(exp, Entities.GeneExpressionLevel)
                                                                            for exp in entity.exp_levels],
                                  })

    def __get_gene_annotations(self):
        gene_manager = GeneAnnotationManager()
        gene_annotations = gene_manager.get_many(FeListGeneAnnotation(is_paged=False), {'synonyms': 0})

        if gene_annotations:
            raise Exception('Error in getting gene annotations. Verify if there are gene annotation stored in the system.')

        self.__gene_annotations = dict(map(lambda g: (g.id_entrez, g.symbol)))

    def __get_id_entrez_gene(self, symbol):
        return next([gene_annotation.id_entrez for gene_annotation in
                     self.__gene_annotations if gene_annotation.symbol == symbol],
                    None)