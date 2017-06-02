from typing import List

from Src.BioDataManagement.DataAccess.Entities.BiologicalSampleBase import BiologicalSampleBase


class MicroRnaSample(BiologicalSampleBase):
    """description of class"""

    def __init__(self, **kargs):
        """

        :param kargs: 
        """
        super().__init__(**kargs)

        self.__exp_levels = kargs.get('exp_levels')

        if self.__exp_levels:
            self.__exp_levels = list(set(self.__exp_levels))

    def __hash__(self):
        return hash(self.patient_id)

    def __eq__(self, other):
        return isinstance(other, MicroRnaSample) and \
               self.patient_id == other.patient_id

    @property
    def exp_levels(self)-> List:
        """description of property"""
        return self.__exp_levels[:]

    @exp_levels.setter
    def exp_levels(self, value: List):
        """

        :param value: 
        :return: 
        """
        self.__exp_levels = list(set(value))

    def validate(self):
        super().validate()

        for g in self.__exp_levels:
            g.validate()

    def as_dict(self):
        sample_dict = super().as_dict()
        return sample_dict.update({'exp_levels': self.__exp_levels})
