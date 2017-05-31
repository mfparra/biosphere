import os
import re

from Src.BioDataFileManagement.CrossCutting.Contracts.DnaMethylationSampleFileRepositoryBase import \
    DnaMethylationSampleFileRepositoryBase
from Src.BioDataFileManagement.CrossCutting.Entities.DnaMethylationLevel import DnaMethylationLevel
from Src.BioDataFileManagement.CrossCutting.Entities.DnaMethylationSampleFile import DnaMethylationSampleFile
from Src.BioDataFileManagement.CrossCutting.Filters.FeListDnaMethylationSampleFile import FeListDnaMethylationSampleFile
from Src.Core.File.FileUtils import FileUtils


class DnaMethylationSampleFileRepository(DnaMethylationSampleFileRepositoryBase):
    """description of class"""

    def __init__(self, directory):
        """
        
        :param directory: 
        """
        super().__init__(directory)
        self.__re = re.compile('^(?P<gene_symbol>\S+)\t(?P<control_value>\d+\.?\d+)\t(?P<case_value>\\d+\.?\d+)')

    def get(self, fe_dna_methylation: FeListDnaMethylationSampleFile) -> FeListDnaMethylationSampleFile:
        """
        
        :param fe_dna_methylation: 
        :return: 
        """
        result_list = None
        directory = os.path.join(self._directory,
                                 fe_dna_methylation.sub_directory) if fe_dna_methylation.sub_directory\
                                                                   else self._directory
        if not fe_dna_methylation.is_paged:
            result_list = FileUtils.read_all(directory, fe_dna_methylation.pattern)
        else:
            fe_dna_methylation.current_page, \
            fe_dna_methylation. page_count, \
            result_list = FileUtils.read_with_pagginate(directory,
                                                        fe_dna_methylation.page_size,
                                                        fe_dna_methylation.current_page, fe_dna_methylation. page_count,
                                                        '\S+.*\.txt')

        for patient_id, dna_methylation_levels in result_list.items():
            levels = []

            for dna_methylation_level in dna_methylation_levels.split('\n'):
                dm_level_match = self.__re.match(dna_methylation_level)

                if not dm_level_match:
                    continue

                dm_level_match = dm_level_match.groupdict()
                levels.append(DnaMethylationLevel(gene_symbol= dm_level_match['gene_symbol'],
                                                  control_value=float(dm_level_match['control_value']),
                                                  case_value=float(dm_level_match['case_value'])))

            fe_dna_methylation.result_list.append(DnaMethylationSampleFile(patient_id=patient_id,
                                                                           dna_methylation_levels=levels))

        return fe_dna_methylation
