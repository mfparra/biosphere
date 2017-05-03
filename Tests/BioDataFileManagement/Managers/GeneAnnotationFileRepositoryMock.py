from Src.BioDataFileManagement.CrossCutting.Contracts.GeneAnnotationFileRepositoryBase import \
    GeneAnnotationFileRepositoryBase
from Src.BioDataFileManagement.CrossCutting.Entities.GeneAnnotation import GeneAnnotation
from Src.BioDataFileManagement.CrossCutting.Filters.FeSingleGeneAnnotation import FeSingleGeneAnnotation


class GeneAnnotaionFileRepositoryMock(GeneAnnotationFileRepositoryBase):
    def __init__(self, directory):
        super().__init__(directory)

    def get(self, fe_gene_annotation: FeSingleGeneAnnotation) -> FeSingleGeneAnnotation:
        fe_gene_annotation.result = [GeneAnnotation(id_entrez=12, symbol='A2MP1',
                                                    synonyms_genes=['A2MD', 'CPAMD5', 'FWP007', 'S863-7']),
                                     GeneAnnotation(id_entrez=121, symbol='ACACB',
                                                    synonyms_genes=['HEL70']),
                                     GeneAnnotation(id_entrez=1, symbol='RPS10-NUDT3',
                                                    synonyms_genes=['-']),
                                     GeneAnnotation(id_entrez=89, symbol='AANAT',
                                                    synonyms_genes=['-'])]

        return fe_gene_annotation


