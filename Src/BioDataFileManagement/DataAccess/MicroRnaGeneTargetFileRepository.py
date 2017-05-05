import re
from os.path import join

from Src.BioDataFileManagement.CrossCutting.Contracts.MicroRnaGeneTargetFileRepositoryBase import \
    MicroRnaGeneTargetFileRepositoryBase
from Src.BioDataFileManagement.CrossCutting.Entities.GeneAnnotation import GeneAnnotation
from Src.BioDataFileManagement.CrossCutting.Entities.MicroRnaGeneTarget import MicroRnaGeneTarget
from Src.BioDataFileManagement.CrossCutting.Filters.FeSingleMicroRnaGeneTarget import FeSingleMicroRnaGeneTarget
from Src.Core.File.FileUtils import FileUtils


class MicroRnaGeneTargetFileRepository(MicroRnaGeneTargetFileRepositoryBase):
    """description of class"""

    def __init__(self, directory):
        """
        
        :param directory: 
        """
        super().__init__(directory)
        self.__re = re.compile('^(?P<mirtarbase_id>\S+)\t(?P<mirna>\S+)\t(?P<species_mirna>[^\t]+)\t(?P<target_gene>\S+'
                               ')\t(?P<target_entrez_gene_id>\d+)\t(?P<species_target_gene>[^\t]+)\t(?P<experiments>\S+'
                               ')\t(?P<support_type>[^\t]+)\t(?P<references_pmid>\d+)')

    def get(self, fe_target: FeSingleMicroRnaGeneTarget) -> FeSingleMicroRnaGeneTarget:
        """
        
        :param fe_target: 
        :return: 
        """
        micro_gene_target_file = FileUtils.read(join(self._directory, fe_target.file))
        microrna_gene_targets = []

        for target in micro_gene_target_file.split('\n'):
            target_match = self.__re.match(target)

            if not target_match:
                continue

            target_match = target_match.groupdict()
            microrna_gene_targets.append(MicroRnaGeneTarget(microrna_symbol=target_match['mirna'],
                                                            gene_target=GeneAnnotation(
                                                                id_entrez=int(target_match['target_entrez_gene_id']),
                                                                symbol=target_match['target_gene'])))

        fe_target.result = microrna_gene_targets
        return fe_target
