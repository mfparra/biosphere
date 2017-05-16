import shutil
import tempfile
import unittest

from os import path

from Src.BioDataFileManagement.CrossCutting.Filters.FeSingleGeneAnnotationFile import FeSingleGeneAnnotationFile
from Src.BioDataFileManagement.DataAccess.GeneAnnotationFileRepository import GeneAnnotationFileRepository


class GeneAnnotationFileRepositoryTest(unittest.TestCase):
    def setUp(self):
        self.__repository_dir = tempfile.mkdtemp()
        self.__content = '#tax_id	GeneID	Symbol	LocusTag	Synonyms	dbXrefs	chromosome	map_location	description	type_of_gene	Symbol_from_nomenclature_authority	Full_name_from_nomenclature_authority	Nomenclature_status	Other_designations	Modification_date\n' \
                         '9606	1	A1BG	-	A1B|ABG|GAB|HYST2477	MIM:138670|HGNC:HGNC:5|Ensembl:ENSG00000121410|HPRD:00726|Vega:OTTHUMG00000183507	19	19q13.4	alpha-1-B glycoprotein	protein-coding	A1BG	alpha-1-B glycoprotein	O	HEL-S-163pA|epididymis secretory sperm binding protein Li 163pA	20160808\n' \
                         '9606	2	A2M	-	A2MD|CPAMD5|FWP007|S863-7	MIM:103950|HGNC:HGNC:7|Ensembl:ENSG00000175899|HPRD:00072|Vega:OTTHUMG00000150267	12	12p13.31	alpha-2-macroglobulin	protein-coding	A2M	alpha-2-macroglobulin	O	C3 and PZP-like alpha-2-macroglobulin domain-containing protein 5|alpha-2-M	20160811\n' \
                         '9606	3	A2MP1	-	A2MP	HGNC:HGNC:8|Ensembl:ENSG00000256069	12	12p13.31	alpha-2-macroglobulin pseudogene 1	pseudo	A2MP1	alpha-2-macroglobulin pseudogene 1	O	pregnancy-zone protein pseudogene	20160808\n' \
                         '9606	9	NAT1	-	AAC1|MNAT|NAT-1|NATI	MIM:108345|HGNC:HGNC:7645|Ensembl:ENSG00000171428|HPRD:00149|Vega:OTTHUMG00000097001	8	8p22	N-acetyltransferase 1	protein-coding	NAT1	N-acetyltransferase 1	O	N-acetyltransferase 1 (arylamine N-acetyltransferase)|N-acetyltransferase type 1|arylamide acetylase 1|monomorphic arylamine N-acetyltransferase	20160808\n' \
                         '9606	10	NAT2	-	AAC2|NAT-2|PNAT	MIM:612182|HGNC:HGNC:7646|Ensembl:ENSG00000156006|HPRD:02000|Vega:OTTHUMG00000130826	8	8p22	N-acetyltransferase 2	protein-coding	NAT2	N-acetyltransferase 2	O	N-acetyltransferase 2 (arylamine N-acetyltransferase)|N-acetyltransferase type 2|arylamide acetylase 2	20160813\n' \
                         '9606	11	NATP	-	AACP|NATP1	HGNC:HGNC:15	8	8p22	N-acetyltransferase pseudogene	pseudo	NATP	N-acetyltransferase pseudogene	O	arylamide acetylase pseudogene	20160806\n' \
                         '9606	12	SERPINA3	-	AACT|ACT|GIG24|GIG25	MIM:107280|HGNC:HGNC:16|Ensembl:ENSG00000196136|Ensembl:ENSG00000273259|HPRD:00120|Vega:OTTHUMG00000029851	14	14q32.1	serpin family A member 3	protein-coding	SERPINA3	serpin family A member 3	O	cell growth-inhibiting gene 24/25 protein|growth-inhibiting protein 24|growth-inhibiting protein 25|serine (or cysteine) proteinase inhibitor, clade A, member 3|serpin A3|serpin peptidase inhibitor, clade A (alpha-1 antiproteinase, antitrypsin), member 3	20160808\n' \
                         '9606	13	AADAC	-	CES5A1|DAC	MIM:600338|HGNC:HGNC:17|Ensembl:ENSG00000114771|HPRD:02640|Vega:OTTHUMG00000159876	3	3q25.1	arylacetamide deacetylase	protein-coding	AADAC	arylacetamide deacetylase	O	arylacetamide deacetylase (esterase)	20160808\n' \
                         '9606	14	AAMP	-	-	MIM:603488|HGNC:HGNC:18|Ensembl:ENSG00000127837|HPRD:04600|Vega:OTTHUMG00000155202	2	2q35	angio associated migratory cell protein	protein-coding	AAMP	angio associated migratory cell protein	O	angio-associated, migratory cell protein	20160808\n' \
                         '9606	15	AANAT	-	DSPS|SNAT	MIM:600950|HGNC:HGNC:19|Ensembl:ENSG00000129673|HPRD:02974|Vega:OTTHUMG00000180179	17	17q25.1	aralkylamine N-acetyltransferase	protein-coding	AANAT	aralkylamine N-acetyltransferase	O	arylalkylamine N-acetyltransferase|serotonin acetylase	20160808\n' \
                         '9606	16	AARS	-	CMT2N|EIEE29	MIM:601065|HGNC:HGNC:20|Ensembl:ENSG00000090861|HPRD:03042|Vega:OTTHUMG00000177042	16	16q22	alanyl-tRNA synthetase	protein-coding	AARS	alanyl-tRNA synthetase	O	alaRS|alanine tRNA ligase 1, cytoplasmic|alanyl-tRNA synthetase, cytoplasmic|renal carcinoma antigen NY-REN-42	20160808\n' \
                         '9606	17	AAVS1	-	AAV	MIM:102699|HGNC:HGNC:22	19	19q13|19q13-qter	adeno-associated virus integration site 1	other	AAVS1	adeno-associated virus integration site 1	O	-	20160730\n' \
                         '9606	18	ABAT	-	GABA-AT|GABAT|NPD009	MIM:137150|HGNC:HGNC:23|Ensembl:ENSG00000183044|HPRD:00661|Vega:OTTHUMG00000048201	16	16p13.2	4-aminobutyrate aminotransferase	protein-coding	ABAT	4-aminobutyrate aminotransferase	O	(S)-3-amino-2-methylpropionate transaminase|4-aminobutyrate transaminase|GABA aminotransferase|GABA transaminase|GABA transferase|gamma-amino-N-butyrate transaminase	20160808\n' \
                         '9606	19	ABCA1	-	ABC-1|ABC1|CERP|HDLDT1|TGD	MIM:600046|HGNC:HGNC:29|Ensembl:ENSG00000165029|HPRD:02501|Vega:OTTHUMG00000020417	9	9q31.1	ATP binding cassette subfamily A member 1	protein-coding	ABCA1	ATP binding cassette subfamily A member 1	O	ATP-binding cassette transporter A1|ATP-binding cassette, sub-family A (ABC1), member 1|cholesterol efflux regulatory protein|membrane-bound	20160811\n' \
                         '9606	20	ABCA2	-	ABC2	MIM:600047|HGNC:HGNC:32|Ensembl:ENSG00000107331|HPRD:08967|Vega:OTTHUMG00000020958	9	9q34	ATP binding cassette subfamily A member 2	protein-coding	ABCA2	ATP binding cassette subfamily A member 2	O	ATP-binding cassette 2|ATP-binding cassette transporter 2|ATP-binding cassette, sub-family A (ABC1), member 2|ATP-binding cassette, sub-family A, member 2	20160808\n' \
                         '9606	21	ABCA3	-	ABC-C|ABC3|EST111653|LBM180|SMDP3	MIM:601615|HGNC:HGNC:33|Ensembl:ENSG00000167972|HPRD:03369|Vega:OTTHUMG00000128845	16	16p13.3	ATP binding cassette subfamily A member 3	protein-coding	ABCA3	ATP binding cassette subfamily A member 3	O	ABC transporter 3|ABC-C transporter|ATP-binding cassette transporter 3|ATP-binding cassette, sub-family A (ABC1), member 3	20160808\n' \
                         '9606	22	ABCB7	-	ABC7|ASAT|Atm1p|EST140535	MIM:300135|HGNC:HGNC:48|Ensembl:ENSG00000131269|HPRD:02137|Vega:OTTHUMG00000021862	X	Xq13.3	ATP binding cassette subfamily B member 7	protein-coding	ABCB7	ATP binding cassette subfamily B member 7	O	ABC transporter 7 protein|ATP-binding cassette sub-family B member 7|ATP-binding cassette transporter 7|ATP-binding cassette, sub-family B (MDR/TAP), member 7	20160808\n'

        self.__synonymous_genes = {
            1: ['A1B', 'ABG', 'GAB', 'HYST2477'],
            2: ['A2MD', 'CPAMD5', 'FWP007', 'S863-7'],
            3: ['A2MP'],
            9: ['AAC1', 'MNAT', 'NAT-1', 'NATI'],
            10: ['AAC2', 'NAT-2', 'PNAT'],
            11: ['AACP', 'NATP1'],
            12: ['-'],
            13: ['CES5A1', 'DAC'],
            14: ['-'],
            15: ['DSPS', 'SNAT'],
            16: ['CMT2N', 'EIEE29'],
            17: ['AAV'],
            18: ['GABA-AT', 'GABAT', 'NPD009'],
            19: ['ABC-1', 'ABC1', 'CERP', 'HDLDT1', 'TGD'],
            20: ['ABC2'],
            21: ['ABC-C', 'ABC3', 'EST111653', 'LBM180', 'SMDP3'],
            22: ['ABC7', 'ASAT', 'Atm1p', 'EST140535']
        }

    def tearDown(self):
        shutil.rmtree(self.__repository_dir)

    def test_get(self):
        with open(path.join(self.__repository_dir, 'gene_annotation.txt'), 'w') as file_temp:
            file_temp.write(self.__content)

        repository = GeneAnnotationFileRepository(self.__repository_dir)
        gene_annotations = repository.get((FeSingleGeneAnnotationFile(file='gene_annotation.txt')))

        self.assertEqual(len(gene_annotations.result), 17)
        self.assertEqual(
            len([g for g in gene_annotations.result if g.id_entrez in [1, 2, 3, 9, 10, 11, 12, 13, 14, 15, 16,
                                                                       17, 18, 19, 20, 21, 22]]), 17)

        self.assertTrue(
            len([g for g in gene_annotations.result if g.symbol in ['A1BG', 'A2M', 'A2MP1', 'NAT1', 'NAT2', 'NATP',
                                                                    'SERPINA3', 'AADAC', 'AAMP', 'AANAT', 'AARS',
                                                                    'AAVS1', 'ABAT', 'ABCA1', 'ABCA2', 'ABCA3',
                                                                    'ABCB']]), 17)

        self.assertTrue(len([g for g in gene_annotations.result if g.synonyms_genes == self.__synonymous_genes[g.id_entrez]]), 17)


if __name__ == '__main__':
    unittest.main()
