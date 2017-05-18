from Src.BioDataFileManagement.CrossCutting.Entities.BiologicalMeasureTypeBase import BiologicalMeasureTypeBase


class GeneExpressionLevel(BiologicalMeasureTypeBase):
    """description of class"""

    def __init__(self, **kargs):
        """

        :param kargs: 
        """
        super().__init__(**kargs)

        self.__gene_symbol = kargs.get("gene_symbol")

        if not self.__gene_symbol:
            raise ValueError("The 'gene_symbol' is required.")

    def __hash__(self):
        return hash(self.__gene_symbol)

    def __eq__(self, other):
        return isinstance(other, GeneExpressionLevel) and \
               self.__gene_symbol == other.gene_symbol

    @property
    def gene_symbol(self) -> str:
        """description of property"""
        return self.__gene_symbol