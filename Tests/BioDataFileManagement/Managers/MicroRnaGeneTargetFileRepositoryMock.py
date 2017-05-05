from Src.BioDataFileManagement.CrossCutting.Contracts.MicroRnaGeneTargetFileRepositoryBase import \
    MicroRnaGeneTargetFileRepositoryBase
from Src.BioDataFileManagement.CrossCutting.Entities.GeneAnnotation import GeneAnnotation
from Src.BioDataFileManagement.CrossCutting.Entities.MicroRnaGeneTarget import MicroRnaGeneTarget
from Src.BioDataFileManagement.CrossCutting.Filters.FeSingleGeneAnnotation import FeSingleGeneAnnotation
from Src.BioDataFileManagement.CrossCutting.Filters.FeSingleMicroRnaGeneTarget import FeSingleMicroRnaGeneTarget


class MicroRnaGeneTargetFileRepositoryMock(MicroRnaGeneTargetFileRepositoryBase):
    def __init__(self, directory):
        super().__init__(directory)

    def get(self, fe_target: FeSingleMicroRnaGeneTarget) -> FeSingleMicroRnaGeneTarget:
        gene_anotations = [GeneAnnotation(id_entrez=12, symbol='A2MP1',
                                          synonyms_genes=['A2MD', 'CPAMD5', 'FWP007', 'S863-7']),
                           GeneAnnotation(id_entrez=121, symbol='ACACB',
                                          synonyms_genes=['HEL70']),
                           GeneAnnotation(id_entrez=1, symbol='RPS10-NUDT3',
                                          synonyms_genes=['-']),
                           GeneAnnotation(id_entrez=89, symbol='AANAT',
                                          synonyms_genes=['-'])]

        targets = [MicroRnaGeneTarget(microrna_symbol='hsa-miR-93-5p',
                                      gene_target=gene_anotations[0]),
                   MicroRnaGeneTarget(microrna_symbol='hsa-miR-93-5p',
                                      gene_target=gene_anotations[1]),
                   MicroRnaGeneTarget(microrna_symbol='hsa-miR-93-5p',
                                      gene_target=gene_anotations[2]),
                   MicroRnaGeneTarget(microrna_symbol='hsa-miR-93-5p',
                                      gene_target=gene_anotations[3]),
                   MicroRnaGeneTarget(microrna_symbol='hsa-miR-302e',
                                      gene_target=gene_anotations[0]),
                   MicroRnaGeneTarget(microrna_symbol='hsa-miR-302e',
                                      gene_target=gene_anotations[0]),
                   MicroRnaGeneTarget(microrna_symbol='hsa-miR-1277-5p',
                                      gene_target=gene_anotations[0]),
                   MicroRnaGeneTarget(microrna_symbol='hsa-miR-1277-5p',
                                      gene_target=gene_anotations[0])]

        fe_target.result = targets
        return fe_target


