from typing import List


class MicroRnaGeneTargetDto(object):
    """description of class"""

    def __init__(self, **kargs):
        """
        
        :param kargs: 
        """
        self.__id_entrez_genes = kargs.get("id_entrez_genes", [])
        self.__micro_rna_symbol = kargs.get('micro_rna_symbol', '')

    def __hash__(self):
        return hash(self.micro_rna_symbol)

    def __eq__(self, other):
        return isinstance(other, MicroRnaGeneTargetDto) and \
            self.micro_rna_symbol == other.micro_rna_symbol

    @property
    def id_entrez_genes(self) -> List[int]:
        """description of property"""
        return self.__id_entrez_genes[:]

    @id_entrez_genes.setter
    def id_entrez_genes(self, value:List[int]):
        """
        
        :param value: 
        :return: 
        """
        self.__id_entrez_genes = value

    @property
    def micro_rna_symbol(self) -> str:
        """description of property"""
        return self.__micro_rna_symbol

    @micro_rna_symbol.setter
    def micro_rna_symbol(self, value:str):
        """

        :param value: 
        :return: 
        """
        self.__micro_rna_symbol = value