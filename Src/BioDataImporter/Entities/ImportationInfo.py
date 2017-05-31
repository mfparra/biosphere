from typing import List

from Src.BioDataImporter.Entities.ImportationStatus import ImportationStatus


class ImportationInfo(object):
    """"""
    def __init__(self, **kargs):
        """
        
        :param kargs: 
        """
        self.__status = kargs.get('status')
        self.__message = kargs.get('message')
        self.__details = kargs.get('details')

        if not self.__status:
            raise ValueError('The status is required.')

        if not self.__message:
            raise ValueError('The message is required.')

        if not self.__details:
            raise ValueError('The details is invalid value.')

    @property
    def status(self) -> ImportationStatus:
        """description of property"""
        return self.__status

    @property
    def message(self) -> str:
        """description of property"""
        return self.__message

    @property
    def details(self) -> List[str]:
        """description of property"""
        return self.__details[:]

