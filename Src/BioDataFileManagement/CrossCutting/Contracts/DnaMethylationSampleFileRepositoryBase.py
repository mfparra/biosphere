from abc import ABCMeta, abstractmethod

from Src.BioDataFileManagement.CrossCutting.Filters.FeListDnaMethylationSampleFile import FeListDnaMethylationSampleFile
from Src.Core.Data.FileRepositoryBase import FileRepositoryBase


class DnaMethylationSampleFileRepositoryBase(FileRepositoryBase, metaclass=ABCMeta):
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
    def get(self, fe_dna_methylation: FeListDnaMethylationSampleFile) -> FeListDnaMethylationSampleFile:
        """

        :param fe_dna_methylation: 
        :return: 
        """
        pass
