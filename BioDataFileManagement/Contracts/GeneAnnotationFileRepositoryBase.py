from abc import ABCMeta, abstractmethod

from os.path import join

from Core.Data.FileRepositoryBase import FileRepositoryBase


class GeneAnnotationFileRepositoryBase(FileRepositoryBase, metaclass=ABCMeta):
    """
    Class responsible for manipulates gene annotation file
    """

    def __init__(self, root_path):
        """
        Constructor.
        :param root_path: 
        """

        super().__init__(join(root_path, 'gene'))

    @abstractmethod
    def get(self, fe_list_gene: FeListGene) -> FeListGene:
        pass
