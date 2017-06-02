from typing import List

from Src.BioDataManagement.DataAccess.Entities.BiologicalSampleBase import BiologicalSampleBase


class DnaMethylationSample(BiologicalSampleBase):
    """description of class"""

    def __init__(self, **kargs):
        """

        :param kargs: 
        """
        super().__init__(**kargs)

        self.__levels = kargs.get('levels')

        if self.__levels:
            self.__levels = list(set(self.__levels))

    def __hash__(self):
        return hash(self.patient_id)

    def __eq__(self, other):
        return isinstance(other, DnaMethylationSample) and \
               self.patient_id == other.patient_id

    @property
    def levels(self)-> List:
        """description of property"""
        return self.__levels[:]

    @levels.setter
    def levels(self, value: List):
        """

        :param value: 
        :return: 
        """
        self.__levels = list(set(value))

    def validate(self):
        super().validate()

        for g in self.__levels:
            g.validate()

    def as_dict(self):
        sample_dict = super().as_dict()
        return sample_dict.update({'levels': self.__levels})
