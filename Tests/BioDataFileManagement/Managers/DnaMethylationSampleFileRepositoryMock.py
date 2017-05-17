from Src.BioDataFileManagement.CrossCutting.Contracts.DnaMethylationSampleFileRepositoryBase import \
    DnaMethylationSampleFileRepositoryBase
from Src.BioDataFileManagement.CrossCutting.Entities.DnaMethylationLevel import DnaMethylationLevel
from Src.BioDataFileManagement.CrossCutting.Entities.DnaMethylationSampleFile import DnaMethylationSampleFile
from Src.BioDataFileManagement.CrossCutting.Filters.FeListDnaMethylationSampleFile import FeListDnaMethylationSampleFile


class DnaMethylationSampleFileRepositoryMock(DnaMethylationSampleFileRepositoryBase):
    def __init__(self, directory):
        super().__init__(directory)

    def get(self, fe_dna_methylation: FeListDnaMethylationSampleFile) -> FeListDnaMethylationSampleFile:
        dna_mthylation_levels = [DnaMethylationLevel(gene_symbol='ABC',
                                                     control_value=1.21,
                                                     case_value=2.3),
                                 DnaMethylationLevel(gene_symbol='ABC',
                                                     control_value=1.2,
                                                     case_value=2.3),
                                 DnaMethylationLevel(gene_symbol='AKS2',
                                                     control_value=0.21,
                                                     case_value=2.3),
                                 DnaMethylationLevel(gene_symbol='AHD1',
                                                     control_value=0.31,
                                                     case_value=2.3),
                                 DnaMethylationLevel(gene_symbol='ABCQ',
                                                     control_value=4.09,
                                                     case_value=4.3)]

        fe_dna_methylation.result_list = [DnaMethylationSampleFile(patient_id='TCGA-A7-A0D9',
                                                                   dna_methylation_levels=dna_mthylation_levels),
                                          DnaMethylationSampleFile(patient_id='TCGA-A7-A0DC',
                                                                   dna_methylation_levels=dna_mthylation_levels),
                                          DnaMethylationSampleFile(patient_id='TCGA-AC-A23H',
                                                                   dna_methylation_levels=dna_mthylation_levels),
                                          DnaMethylationSampleFile(patient_id='TCGA-BH-A0B8',
                                                                   dna_methylation_levels=dna_mthylation_levels),
                                          DnaMethylationSampleFile(patient_id='TCGA-A7-A0DC',
                                                                   dna_methylation_levels=dna_mthylation_levels)]

        return fe_dna_methylation


