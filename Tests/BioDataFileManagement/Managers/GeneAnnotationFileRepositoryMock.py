from Src.BioDataFileManagement.CrossCutting.Contracts.GeneAnnotationFileRepositoryBase import \
    GeneAnnotationFileRepositoryBase
from Src.BioDataFileManagement.CrossCutting.Entities.GeneAnnotationFile import GeneAnnotationFile
from Src.BioDataFileManagement.CrossCutting.Filters.FeSingleGeneAnnotationFile import FeSingleGeneAnnotationFile


class GeneAnnotaionFileRepositoryMock(GeneAnnotationFileRepositoryBase):
    def __init__(self, directory):
        super().__init__(directory)

    def get(self, fe_gene_annotation: FeSingleGeneAnnotationFile) -> FeSingleGeneAnnotationFile:
        fe_gene_annotation.result = [GeneAnnotationFile(id_entrez=12, symbol='A2MP1',
                                                        synonyms_genes=['A2MD', 'CPAMD5', 'FWP007', 'S863-7']),
                                     GeneAnnotationFile(id_entrez=121, symbol='ACACB',
                                                        synonyms_genes=['HEL70']),
                                     GeneAnnotationFile(id_entrez=1, symbol='RPS10-NUDT3',
                                                        synonyms_genes=['-']),
                                     GeneAnnotationFile(id_entrez=89, symbol='AANAT',
                                                        synonyms_genes=['-'])]

        return fe_gene_annotation


