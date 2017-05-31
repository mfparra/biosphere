import os
import re

from Src.BioDataFileManagement.CrossCutting.Contracts.MicroRnaSampleFileRepositoryBase import \
    MicroRnaSampleFileRepositoryBase
from Src.BioDataFileManagement.CrossCutting.Entities.MicroRnaExpressionLevel import MicroRnaExpressionLevel
from Src.BioDataFileManagement.CrossCutting.Entities.MicroRnaSampleFile import MicroRnaSampleFile
from Src.BioDataFileManagement.CrossCutting.Filters.FeListMicroRnaSampleFile import FeListMicroRnaSampleFile
from Src.Core.File.FileUtils import FileUtils


class MicroRnaSampleFileRepository(MicroRnaSampleFileRepositoryBase):
    """description of class"""

    def __init__(self, directory):
        """
        
        :param directory: 
        """
        super().__init__(directory)
        self.__re = re.compile('^(?P<symbol>\S+)\t(?P<control_value>\d+\.?\d+)\t(?P<case_value>\\d+\.?\d+)')

    def get(self, fe_mirna: FeListMicroRnaSampleFile) -> FeListMicroRnaSampleFile:
        """
        
        :param fe_mrna: 
        :return: 
        """
        result_list = None
        directory = os.path.join(self._directory,
                                 fe_mirna.sub_directory) if fe_mirna.sub_directory \
                                                         else self._directory

        if not fe_mirna.is_paged:
            result_list = FileUtils.read_all(directory, fe_mirna.pattern)
        else:
            fe_mirna.current_page, \
            fe_mirna. page_count, \
            result_list = FileUtils.read_with_pagginate(directory,
                                                        fe_mirna.page_size,
                                                        fe_mirna.current_page, fe_mirna. page_count,
                                                        '\S+.*\.txt')

        for patient_id, mirna_expression_levels in result_list.items():
            levels = []

            for mirna_expression_level in mirna_expression_levels.split('\n'):
                mirna_level_match = self.__re.match(mirna_expression_level)

                if not mirna_level_match:
                    continue

                ge_level_match = mirna_level_match.groupdict()
                levels.append(MicroRnaExpressionLevel(symbol= mirna_level_match['symbol'],
                                                      control_value=float(mirna_level_match['control_value']),
                                                      case_value=float(mirna_level_match['case_value'])))

            fe_mirna.result_list.append(MicroRnaSampleFile(patient_id=patient_id,
                                                           micro_rna_expression_levels=levels))

        return fe_mirna
