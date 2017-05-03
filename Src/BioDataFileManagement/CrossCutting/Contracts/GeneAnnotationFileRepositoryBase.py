from abc import ABCMeta, abstractmethod

from Src.Core.Data.FileRepositoryBase import FileRepositoryBase

from Src.BioDataFileManagement.CrossCutting.Filters.FeSingleGeneAnnotation import FeSingleGeneAnnotation


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
