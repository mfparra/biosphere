import re
from os.path import join

from Src.Core.File.FileUtils import FileUtils

from Src.BioDataFileManagement.CrossCutting.Filters.FeSingleGeneAnnotationFile import FeSingleGeneAnnotationFile
from Src.BioDataFileManagement.CrossCutting.Entities.GeneAnnotationFile import GeneAnnotationFile
from Src.BioDataFileManagement.CrossCutting.Contracts.GeneAnnotationFileRepositoryBase import \
    GeneAnnotationFileRepositoryBase


class GeneAnnotationFileRepository(GeneAnnotationFileRepositoryBase):
    """description of class"""

    def __init__(self, directory):
        """
        
        :param directory: 
        """
        super().__init__(directory)
        self.__re = re.compile('^(?P<tax_id>\d+)\t(?P<gene_id>\d+)\t(?P<symbol>\S+)\t(?P<locus_tag>\S+)\t('
                               '?P<synonyms>\S+)\t(?P<dbXrefs>\S+)\t(?P<chromosome>\d+|X|Y)\t(?P<map_location>\S+)\t('
                               '?P<description>[^\t]+)\t(?P<type_of_gene>\S+)\t('
                               '?P<symbol_from_nomenclature_authority>\S+)\t('
                               '?P<full_name_from_nomenclature_authority>[^\t]+)\t(?P<nomenclature_status>\S)\t('
                               '?P<other_designations>[^\t]+)\t(?P<modification_date>\d{8})')

    def get(self, fe_gene_annotation: FeSingleGeneAnnotationFile) -> FeSingleGeneAnnotationFile:
        """
        
        :param fe_gene_annotation: 
        :return: 
        """
        ga_file = FileUtils.read(join(self._directory, fe_gene_annotation.file))
        gene_annotations = []

        for gene in ga_file.split('\n'):
            gene_match = self.__re.match(gene)

            if not gene_match:
                continue

            gene_match = gene_match.groupdict()
            gene_annotations.append(GeneAnnotationFile(id_entrez=int(gene_match['gene_id']),
                                                       symbol=gene_match['symbol'],
                                                       synonyms_genes=gene_match['synonyms'].split('|')))

        fe_gene_annotation.result = gene_annotations
        return fe_gene_annotation
