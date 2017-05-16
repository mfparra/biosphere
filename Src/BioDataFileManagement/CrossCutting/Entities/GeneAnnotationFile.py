from typing import List


class GeneAnnotationFile(object):
    """description of class"""

    def __init__(self, **kargs):
        """description of initialize"""

        if not kargs.get('symbol'):
            raise ValueError("The 'symbol' is required.")

        if not kargs.get('id_entrez'):
            raise ValueError("The 'id_entrez' is required.")

        if kargs.get('id_entrez') < 0:
            raise ValueError("The 'id_entrez' is invalid value.")

        self.__symbol = kargs.get('symbol').upper()
        self.__id_entrez = kargs.get('id_entrez')

        if kargs.get('synonyms_genes', None):
            self.__synonyms_genes = [g.upper() for g in kargs.get('synonyms_genes')]
            self.__synonyms_genes = list(set(self.__synonyms_genes))
        else:
            self.__synonyms_genes = []

    def __hash__(self):
        return hash((self.__symbol, self.id_entrez))

    def __eq__(self, other):
        return isinstance(other, GeneAnnotationFile) and \
               self.__symbol == other.symbol and \
               self.__id_entrez == other.id_entrez

    @property
    def symbol(self) -> str:
        """description of property"""
        return self.__symbol

    @property
    def synonyms_genes(self) -> List[str]:
        """description of property"""
        return self.__synonyms_genes

    @property
    def id_entrez(self) -> int:
        """description of property"""
        return self.__id_entrez
