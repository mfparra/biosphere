from typing import List

from Src.Core.Entity.EntityBase import EntityBase


class GeneAnnotation(EntityBase):
    """description of class"""

    def __init__(self, **kargs):
        """

        :param kargs: 
        """
        self.__id_entrez = kargs.get('id_entrez')
        self.__symbol = kargs.get('symbol')
        self.__synonyms_genes = kargs.get('synonyms_genes', [])

    def __hash__(self):
        return hash(self.id_entrez)

    def __eq__(self, other):
        return isinstance(other, GeneAnnotation) and \
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

    def validate(self):
        if not self.__id_entrez:
            raise ValueError('Id entrez is required.')
        if self.__id_entrez <= 0:
            raise ValueError('Id entrez requires value greater than 0.')

        if not self.__symbol:
            raise ValueError('Symbol is required.')

    def as_dict(self):
        return {'id_entrez': self.__id_entrez,
                'symbol': self.__symbol,
                'synonyms_genes': self.__synonyms_genes}