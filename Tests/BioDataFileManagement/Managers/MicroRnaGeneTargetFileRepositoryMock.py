from Src.BioDataFileManagement.CrossCutting.Contracts.MicroRnaGeneTargetFileRepositoryBase import \
    MicroRnaGeneTargetFileRepositoryBase
from Src.BioDataFileManagement.CrossCutting.Entities.GeneAnnotationFile import GeneAnnotationFile
from Src.BioDataFileManagement.CrossCutting.Entities.MicroRnaGeneTargetFile import MicroRnaGeneTargetFile
from Src.BioDataFileManagement.CrossCutting.Filters.FeSingleMicroRnaGeneTargetFile import FeSingleMicroRnaGeneTargetFile


class MicroRnaGeneTargetFileRepositoryMock(MicroRnaGeneTargetFileRepositoryBase):
    def __init__(self, directory):
        super().__init__(directory)

    def get(self, fe_target: FeSingleMicroRnaGeneTargetFile) -> FeSingleMicroRnaGeneTargetFile:
        gene_anotations = [GeneAnnotationFile(id_entrez=12, symbol='A2MP1',
                                              synonyms_genes=['A2MD', 'CPAMD5', 'FWP007', 'S863-7']),
                           GeneAnnotationFile(id_entrez=121, symbol='ACACB',
                                              synonyms_genes=['HEL70']),
                           GeneAnnotationFile(id_entrez=1, symbol='RPS10-NUDT3',
                                              synonyms_genes=['-']),
                           GeneAnnotationFile(id_entrez=89, symbol='AANAT',
                                              synonyms_genes=['-'])]

        targets = [MicroRnaGeneTargetFile(microrna_symbol='hsa-miR-93-5p',
                                          gene_target=gene_anotations[0]),
                   MicroRnaGeneTargetFile(microrna_symbol='hsa-miR-93-5p',
                                          gene_target=gene_anotations[1]),
                   MicroRnaGeneTargetFile(microrna_symbol='hsa-miR-93-5p',
                                          gene_target=gene_anotations[2]),
                   MicroRnaGeneTargetFile(microrna_symbol='hsa-miR-93-5p',
                                          gene_target=gene_anotations[3]),
                   MicroRnaGeneTargetFile(microrna_symbol='hsa-miR-302e',
                                          gene_target=gene_anotations[0]),
                   MicroRnaGeneTargetFile(microrna_symbol='hsa-miR-302e',
                                          gene_target=gene_anotations[0]),
                   MicroRnaGeneTargetFile(microrna_symbol='hsa-miR-1277-5p',
                                          gene_target=gene_anotations[0]),
                   MicroRnaGeneTargetFile(microrna_symbol='hsa-miR-1277-5p',
                                          gene_target=gene_anotations[0])]

        fe_target.result = targets
        return fe_target


