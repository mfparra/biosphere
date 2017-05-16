from Src.BioDataFileManagement.CrossCutting.Entities.GeneAnnotationFile import GeneAnnotationFile


class MicroRnaGeneTargetFile(object):
    """description of class"""

    def __init__(self, **kargs):
        """description of initialize"""

        if not kargs.get('microrna_symbol'):
            raise ValueError("The 'microrna_symbol' is required.")

        if not kargs.get('gene_target'):
            raise ValueError("The 'gene_target' is required.")

        self.__microrna_symbol = kargs.get('microrna_symbol').upper()
        self.__gene_target = kargs.get('gene_target')

    def __hash__(self):
        return hash((self.__microrna_symbol, self.__gene_target))

    def __eq__(self, other):
        return isinstance(other, MicroRnaGeneTargetFile) and \
               self.__microrna_symbol == other.microrna_symbol and \
               self.__gene_target == other.gene_target

    @property
    def microrna_symbol(self) -> str:
        """description of property"""
        return self.__microrna_symbol

    @property
    def gene_target(self) -> GeneAnnotationFile:
        """description of property"""
        return self.__gene_target
