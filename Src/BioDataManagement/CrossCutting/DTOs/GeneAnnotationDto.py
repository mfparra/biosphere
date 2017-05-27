from typing import List


class GeneAnnotationDto(object):
    """description of class"""

    def __init__(self, **kargs):
        """
        
        :param kargs: 
        """

        self.__id_entrez = kargs.get('id_entrez', None)
        self.__symbol = kargs.get('symbol', '')
        self.__synonyms_genes = kargs.get('synonyms_genes', [])

    def __hash__(self):
        return hash(self.id_entrez)

    def __eq__(self, other):
        return isinstance(other, GeneAnnotationDto) and \
            self.id_entrez == other.id_entrez

    @property
    def id_entrez(self) -> int:
        """description of property"""
        return self.__id_entrez

    @id_entrez.setter
    def id_entrez(self, value):
        """
        
        :param value: 
        :return: 
        """
        self.__id_entrez = value

    @property
    def symbol(self) -> str:
        """description of property"""
        return self.__symbol

    @symbol.setter
    def symbol(self, value):
        """

        :param value: 
        :return: 
        """
        self.__symbol = value

    @property
    def synonyms_genes(self) -> List[str]:
        """description of property"""
        return self.__synonyms_genes[:]

    @synonyms_genes.setter
    def synonyms_genes(self, value):
        """

        :param value: 
        :return: 
        """
        self.__synonyms_genes = value