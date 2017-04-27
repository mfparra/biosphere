from abc import ABCMeta, abstractmethod

from BioDataFileManagement.CrossCutting.Filters.FeSingleGeneAnnotation import FeSingleGeneAnnotation
from Core.Data.FileRepositoryBase import FileRepositoryBase


class GeneAnnotationFileRepositoryBase(FileRepositoryBase, metaclass=ABCMeta):
    """
    Class responsible for manipulates gene annotation file
    """

    def __init__(self, directory):
        """
        Constructor.
        :param directory: 
        """

        super().__init__(directory)

    @abstractmethod
    def get(self, fe_gene_annotation: FeSingleGeneAnnotation) -> FeSingleGeneAnnotation:
        """

        :param fe_gene_annotation: 
        :return: 
        """
        pass
