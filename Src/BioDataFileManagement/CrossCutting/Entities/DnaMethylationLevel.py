from Src.BioDataFileManagement.CrossCutting.Entities.BiologicalMeasureType import BiologicalMeasureType


class DnaMethylationLevel:
    """description of class"""

    def __init__(self, **kargs):
        """

        :param kargs: 
        """
        self.__biological_measure_type = BiologicalMeasureType(**kargs)
        self.__gene_symbol = kargs.get("gene_symbol")

        if not self.__gene_symbol:
            raise ValueError("The 'gene_symbol' is required.")

    def __hash__(self):
        return hash(self.__gene_symbol)

    def __eq__(self, other):
        return isinstance(other, DnaMethylationLevel) and \
               self.__gene_symbol == other.gene_symbol

    @property
    def gene_symbol(self) -> str:
        """description of property"""
        return self.__gene_symbol

    @property
    def control_value(self) -> float:
        """description of property"""
        return self.__biological_measure_type.control_value

    @property
    def case_value(self) -> float:
        """description of property"""
        return self.__biological_measure_type.case_value