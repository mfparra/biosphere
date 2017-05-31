from Src.BioDataFileManagement.CrossCutting.Entities.BiologicalMeasureTypeBase import BiologicalMeasureTypeBase


class MicroRnaExpressionLevel(BiologicalMeasureTypeBase):
    """description of class"""

    def __init__(self, **kargs):
        """

        :param kargs: 
        """
        super().__init__(**kargs)

        self.__symbol = kargs.get("symbol")

        if not self.__symbol:
            raise ValueError("The 'symbol' is required.")

    def __hash__(self):
        return hash(self.__symbol)

    def __eq__(self, other):
        return isinstance(other, MicroRnaExpressionLevel) and \
               self.__symbol == other.symbol

    @property
    def symbol(self) -> str:
        """description of property"""
        return self.__symbol