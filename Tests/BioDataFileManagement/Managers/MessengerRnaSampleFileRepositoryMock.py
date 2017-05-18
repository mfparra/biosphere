from Src.BioDataFileManagement.CrossCutting.Contracts.MessengerRnaSampleFileRepositoryBase import \
    MessengerRnaSampleFileRepositoryBase
from Src.BioDataFileManagement.CrossCutting.Entities.GeneExpressionLevel import GeneExpressionLevel
from Src.BioDataFileManagement.CrossCutting.Entities.MessengerRnaSampleFile import MessengerRnaSampleFile
from Src.BioDataFileManagement.CrossCutting.Filters.FeListMessengerRnaSampleFile import FeListMessengerRnaSampleFile


class MessengerRnaSampleFileRepositoryMock(MessengerRnaSampleFileRepositoryBase):
    def __init__(self, directory):
        super().__init__(directory)

    def get(self, fe_mrna: FeListMessengerRnaSampleFile) -> FeListMessengerRnaSampleFile:
        gene_expression_levels = [GeneExpressionLevel(gene_symbol='ABC',
                                                      control_value=1.21,
                                                      case_value=2.3),
                                  GeneExpressionLevel(gene_symbol='ABC',
                                                      control_value=1.2,
                                                      case_value=2.3),
                                  GeneExpressionLevel(gene_symbol='AKS2',
                                                      control_value=0.21,
                                                      case_value=2.3),
                                  GeneExpressionLevel(gene_symbol='AHD1',
                                                      control_value=0.31,
                                                      case_value=2.3),
                                  GeneExpressionLevel(gene_symbol='ABCQ',
                                                      control_value=4.09,
                                                      case_value=4.3)]

        fe_mrna.result_list = [MessengerRnaSampleFile(patient_id='TCGA-A7-A0D9',
                                                      gene_expression_levels=gene_expression_levels),
                               MessengerRnaSampleFile(patient_id='TCGA-A7-A0DC',
                                                      gene_expression_levels=gene_expression_levels),
                               MessengerRnaSampleFile(patient_id='TCGA-AC-A23H',
                                                      gene_expression_levels=gene_expression_levels),
                               MessengerRnaSampleFile(patient_id='TCGA-BH-A0B8',
                                                      gene_expression_levels=gene_expression_levels),
                               MessengerRnaSampleFile(patient_id='TCGA-A7-A0DC',
                                                      gene_expression_levels=gene_expression_levels)]

        return fe_mrna


