import shutil
import tempfile
import unittest

from os import path

from Src.BioDataFileManagement.CrossCutting.Filters.FeSingleMicroRnaGeneTargetFile import FeSingleMicroRnaGeneTargetFile
from Src.BioDataFileManagement.DataAccess.MicroRnaGeneTargetFileRepository import MicroRnaGeneTargetFileRepository


class MicroRnaGeneTargetFileRepositoryTest(unittest.TestCase):
    def setUp(self):
        self.__repository_dir = tempfile.mkdtemp()
        self.__content = 'miRTarBaseID	miRNA	Species-(miRNA)	Target-Gene	Target-Gene-(Entrez-Gene-ID)	Species-(Target-Gene)	Experiments	Support Type	References-(PMID)\n'\
                         'MIRT559756	hsa-let-7a-2-3p	Homo sapiens	ABI2	10152	Homo sapiens	PAR-CLIP	Functional MTI (Weak)	21572407\n'\
                         'MIRT619966	hsa-let-7a-2-3p	Homo sapiens	ACSM2B	348158	Homo sapiens	HITS-CLIP	Functional MTI (Weak)	23313552\n'\
                         'MIRT619966	hsa-let-7a-2-3p	Homo sapiens	ACSM2B	348158	Homo sapiens	HITS-CLIP	Functional MTI (Weak)	23824327\n'\
                         'MIRT482251	hsa-let-7a-2-3p	Homo sapiens	AGPAT5	55326	Homo sapiens	PAR-CLIP	Functional MTI (Weak)	23592263\n'\
                         'MIRT226718	hsa-let-7a-2-3p	Homo sapiens	ANP32B	10541	Homo sapiens	PAR-CLIP	Functional MTI (Weak)	20371350\n'\
                         'MIRT226718	hsa-let-7a-2-3p	Homo sapiens	ANP32B	10541	Homo sapiens	PAR-CLIP	Functional MTI (Weak)	23446348\n'\
                         'MIRT084789	hsa-let-7a-2-3p	Homo sapiens	APP	351	Homo sapiens	PAR-CLIP	Functional MTI (Weak)	21572407\n'\
                         'MIRT066782	hsa-let-7a-2-3p	Homo sapiens	ARID1A	8289	Homo sapiens	PAR-CLIP	Functional MTI (Weak)	20371350\n'\
                         'MIRT481551	hsa-let-7a-2-3p	Homo sapiens	ARL10	285598	Homo sapiens	PAR-CLIP	Functional MTI (Weak)	23592263\n'\
                         'MIRT708179	hsa-let-7a-2-3p	Homo sapiens	BACH2	60468	Homo sapiens	HITS-CLIP	Functional MTI (Weak)	21572407\n'\
                         'MIRT617010	hsa-let-7a-2-3p	Homo sapiens	C16orf52	730094	Homo sapiens	HITS-CLIP	Functional MTI (Weak)	23824327\n'\
                         'MIRT562849	hsa-let-7a-2-3p	Homo sapiens	C17orf58	284018	Homo sapiens	PAR-CLIP	Functional MTI (Weak)	20371350\n'\
                         'MIRT480195	hsa-let-7a-2-3p	Homo sapiens	CAD	790	Homo sapiens	PAR-CLIP	Functional MTI (Weak)	23592263\n'\
                         'MIRT058253	hsa-let-7a-2-3p	Homo sapiens	CADM1	23705	Homo sapiens	PAR-CLIP	Functional MTI (Weak)	20371350\n'\
                         'MIRT514028	hsa-let-7a-2-3p	Homo sapiens	CALM2	805	Homo sapiens	PAR-CLIP	Functional MTI (Weak)	20371350\n'\
                         'MIRT514028	hsa-let-7a-2-3p	Homo sapiens	CALM2	805	Homo sapiens	PAR-CLIP	Functional MTI (Weak)	23446348\n'\

    def tearDown(self):
        shutil.rmtree(self.__repository_dir)

    def test_get(self):
        with open(path.join(self.__repository_dir, 'microrna_gene_target.txt'), 'w') as file_temp:
            file_temp.write(self.__content)

        repository = MicroRnaGeneTargetFileRepository(self.__repository_dir)
        targets = repository.get((FeSingleMicroRnaGeneTargetFile(file='microrna_gene_target.txt')))

        self.assertEqual(len(targets.result), 16)
        self.assertEqual(
            len([g for g in targets.result if g.gene_target.id_entrez in [10152, 348158, 55326, 10541, 351, 8289, 285598,
                                                                         60468, 730094, 284018, 790, 23705, 805]]), 16)

        self.assertTrue(
            len([g for g in targets.result if g.gene_target.symbol in ['ABI2', 'ACSM2B', 'AGPAT5', 'ANP32B', 'APP',
                                                                      'ARID1A', 'ARL10', 'BACH2', 'C16orf52', 'C17orf58',
                                                                      'CAD', 'CADM1', 'CALM2']]), 16)


if __name__ == '__main__':
    unittest.main()
