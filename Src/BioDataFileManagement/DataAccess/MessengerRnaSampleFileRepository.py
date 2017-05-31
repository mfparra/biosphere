import os
import re

from Src.BioDataFileManagement.CrossCutting.Contracts.MessengerRnaSampleFileRepositoryBase import \
    MessengerRnaSampleFileRepositoryBase
from Src.BioDataFileManagement.CrossCutting.Entities.GeneExpressionLevel import GeneExpressionLevel
from Src.BioDataFileManagement.CrossCutting.Entities.MessengerRnaSampleFile import MessengerRnaSampleFile
from Src.BioDataFileManagement.CrossCutting.Filters.FeListMessengerRnaSampleFile import FeListMessengerRnaSampleFile
from Src.Core.File.FileUtils import FileUtils


class MessengerRnaSampleFileRepository(MessengerRnaSampleFileRepositoryBase):
    """description of class"""

    def __init__(self, directory):
        """
        
        :param directory: 
        """
        super().__init__(directory)
        self.__re = re.compile('^(?P<gene_symbol>\S+)\t(?P<control_value>\d+\.?\d+)\t(?P<case_value>\\d+\.?\d+)')

    def get(self, fe_mrna: FeListMessengerRnaSampleFile) -> FeListMessengerRnaSampleFile:
        """
        
        :param fe_mrna: 
        :return: 
        """
        result_list = None
        directory = os.path.join(self._directory,
                                 fe_mrna.sub_directory) if fe_mrna.sub_directory \
                                                        else self._directory

        if not fe_mrna.is_paged:
            result_list = FileUtils.read_all(directory, fe_mrna.pattern)
        else:
            fe_mrna.current_page, \
            fe_mrna. page_count, \
            result_list = FileUtils.read_with_pagginate(directory,
                                                        fe_mrna.page_size,
                                                        fe_mrna.current_page, fe_mrna. page_count,
                                                        '\S+.*\.txt')

        for patient_id, gene_expression_levels in result_list.items():
            levels = []

            for gene_expression_level in gene_expression_levels.split('\n'):
                ge_level_match = self.__re.match(gene_expression_level)

                if not ge_level_match:
                    continue

                ge_level_match = ge_level_match.groupdict()
                levels.append(GeneExpressionLevel(gene_symbol= ge_level_match['gene_symbol'],
                                                  control_value=float(ge_level_match['control_value']),
                                                  case_value=float(ge_level_match['case_value'])))

            fe_mrna.result_list.append(MessengerRnaSampleFile(patient_id=patient_id,
                                                              gene_expression_levels=levels))

        return fe_mrna
