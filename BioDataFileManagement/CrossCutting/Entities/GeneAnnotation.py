from typing import List


class GeneAnnotation(object):
    """description of class"""

    def __init__(self, **kargs):
        """description of initialize"""

        if not kargs.get('symbol'):
            raise ValueError("The 'symbol' is required.")

        if not kargs.get('id_entrez'):
            raise ValueError("The 'id_entrez' is required.")

        self.__symbol = kargs.get('symbol').upper()
        self.__id_entrez = kargs.get('id_entrez')

        if self.__synonyms_genes:
            self.__synonyms_genes = [g.upper() for g in kargs.get("synonyms_genes", [])]

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
