"""
kmer_test.py file that runs the unittests for kmer.py when the file is called or
run using the python CLI.

Group Project for CISC 471, Computational Biology.

By:
    - Andrew Ma (20030440)
    - Rayan Shaikli (20059806)
    - Hershil Devnani (20001045)

There are two ways to run the program, outlined below. Both methods run the
unittests.

Sample Usage:
  $ python -m unittest dna_test.py
  $ python -m main main.py
"""

import unittest
from kmer import kmer, format_output
from parsers import parse_gc_data

kmer_num = 4


class TestProgrammingPartOne(unittest.TestCase):
    """Testing class for the required unittests
    """

    def test_kmer_positive_a(self):
        kmer_data = parse_gc_data("rosalind_kmer_1.txt")
        kmer_composition_raw = kmer(kmer_data, kmer_num)
        kmer_composition_formatted = format_output(kmer_composition_raw)

        solution_raw = {'AAAA': 4, 'AAAC': 1, 'AAAG': 4, 'AAAT': 3, 'AACA': 0,
                        'AACC': 1, 'AACG': 1, 'AACT': 5, 'AAGA': 1, 'AAGC': 3,
                        'AAGG': 1, 'AAGT': 2, 'AATA': 2, 'AATC': 1, 'AATG': 2,
                        'AATT': 0, 'ACAA': 1, 'ACAC': 1, 'ACAG': 3, 'ACAT': 1,
                        'ACCA': 2, 'ACCC': 1, 'ACCG': 3, 'ACCT': 1, 'ACGA': 1,
                        'ACGC': 1, 'ACGG': 1, 'ACGT': 2, 'ACTA': 2, 'ACTC': 5,
                        'ACTG': 1, 'ACTT': 3, 'AGAA': 0, 'AGAC': 2, 'AGAG': 2,
                        'AGAT': 1, 'AGCA': 1, 'AGCC': 1, 'AGCG': 1, 'AGCT': 3,
                        'AGGA': 1, 'AGGC': 0, 'AGGG': 0, 'AGGT': 1, 'AGTA': 5,
                        'AGTC': 5, 'AGTG': 1, 'AGTT': 5, 'ATAA': 0, 'ATAC': 2,
                        'ATAG': 0, 'ATAT': 2, 'ATCA': 1, 'ATCC': 2, 'ATCG': 1,
                        'ATCT': 1, 'ATGA': 1, 'ATGC': 2, 'ATGG': 0, 'ATGT': 1,
                        'ATTA': 0, 'ATTC': 0, 'ATTG': 1, 'ATTT': 1, 'CAAA': 3,
                        'CAAC': 2, 'CAAG': 1, 'CAAT': 0, 'CACA': 3, 'CACC': 2,
                        'CACG': 3, 'CACT': 0, 'CAGA': 0, 'CAGC': 2, 'CAGG': 0,
                        'CAGT': 8, 'CATA': 0, 'CATC': 0, 'CATG': 1, 'CATT': 0,
                        'CCAA': 2, 'CCAC': 1, 'CCAG': 3, 'CCAT': 0, 'CCCA': 0,
                        'CCCC': 0, 'CCCG': 1, 'CCCT': 4, 'CCGA': 3, 'CCGC': 2,
                        'CCGG': 1, 'CCGT': 1, 'CCTA': 3, 'CCTC': 1, 'CCTG': 2,
                        'CCTT': 1, 'CGAA': 3, 'CGAC': 1, 'CGAG': 2, 'CGAT': 1,
                        'CGCA': 2, 'CGCC': 1, 'CGCG': 1, 'CGCT': 1, 'CGGA': 2,
                        'CGGC': 3, 'CGGG': 2, 'CGGT': 1, 'CGTA': 1, 'CGTC': 0,
                        'CGTG': 1, 'CGTT': 1, 'CTAA': 3, 'CTAC': 2, 'CTAG': 1,
                        'CTAT': 2, 'CTCA': 6, 'CTCC': 2, 'CTCG': 1, 'CTCT': 1,
                        'CTGA': 1, 'CTGC': 2, 'CTGG': 3, 'CTGT': 3, 'CTTA': 3,
                        'CTTC': 2, 'CTTG': 3, 'CTTT': 0, 'GAAA': 3, 'GAAC': 2,
                        'GAAG': 1, 'GAAT': 1, 'GACA': 0, 'GACC': 0, 'GACG': 1,
                        'GACT': 4, 'GAGA': 3, 'GAGC': 0, 'GAGG': 1, 'GAGT': 5,
                        'GATA': 0, 'GATC': 2, 'GATG': 0, 'GATT': 1, 'GCAA': 2,
                        'GCAC': 1, 'GCAG': 3, 'GCAT': 0, 'GCCA': 1, 'GCCC': 2,
                        'GCCG': 2, 'GCCT': 1, 'GCGA': 1, 'GCGC': 0, 'GCGG': 3,
                        'GCGT': 0, 'GCTA': 0, 'GCTC': 4, 'GCTG': 5, 'GCTT': 0,
                        'GGAA': 3, 'GGAC': 0, 'GGAG': 2, 'GGAT': 1, 'GGCA': 1,
                        'GGCC': 3, 'GGCG': 0, 'GGCT': 3, 'GGGA': 2, 'GGGC': 2,
                        'GGGG': 1, 'GGGT': 1, 'GGTA': 0, 'GGTC': 2, 'GGTG': 1,
                        'GGTT': 0, 'GTAA': 2, 'GTAC': 2, 'GTAG': 1, 'GTAT': 2,
                        'GTCA': 0, 'GTCC': 2, 'GTCG': 2, 'GTCT': 5, 'GTGA': 2,
                        'GTGC': 2, 'GTGG': 1, 'GTGT': 1, 'GTTA': 2, 'GTTC': 1,
                        'GTTG': 2, 'GTTT': 2, 'TAAA': 2, 'TAAC': 2, 'TAAG': 1,
                        'TAAT': 1, 'TACA': 3, 'TACC': 4, 'TACG': 0, 'TACT': 2,
                        'TAGA': 1, 'TAGC': 1, 'TAGG': 0, 'TAGT': 1, 'TATA': 2,
                        'TATC': 2, 'TATG': 1, 'TATT': 1, 'TCAA': 1, 'TCAC': 5,
                        'TCAG': 2, 'TCAT': 0, 'TCCA': 3, 'TCCC': 2, 'TCCG': 1,
                        'TCCT': 1, 'TCGA': 2, 'TCGC': 2, 'TCGG': 3, 'TCGT': 0,
                        'TCTA': 3, 'TCTC': 0, 'TCTG': 1, 'TCTT': 3, 'TGAA': 1,
                        'TGAC': 2, 'TGAG': 3, 'TGAT': 0, 'TGCA': 2, 'TGCC': 1,
                        'TGCG': 2, 'TGCT': 2, 'TGGA': 1, 'TGGC': 2, 'TGGG': 3,
                        'TGGT': 0, 'TGTA': 1, 'TGTC': 2, 'TGTG': 3, 'TGTT': 1,
                        'TTAA': 1, 'TTAC': 3, 'TTAG': 1, 'TTAT': 0, 'TTCA': 1,
                        'TTCC': 1, 'TTCG': 3, 'TTCT': 0, 'TTGA': 2, 'TTGC': 1,
                        'TTGG': 2, 'TTGT': 2, 'TTTA': 0, 'TTTC': 2, 'TTTG': 1,
                        'TTTT': 1}

        solution_formatted = "4 1 4 3 0 1 1 5 1 3 1 2 2 1 2 0 1 1 3 1 2 1 3 1 " \
                             "1 1 1 2 2 5 1 3 0 2 2 1 1 1 1 3 1 0 0 1 5 5 1 5 " \
                             "0 2 0 2 1 2 1 1 1 2 0 1 0 0 1 1 3 2 1 0 3 2 3 0 " \
                             "0 2 0 8 0 0 1 0 2 1 3 0 0 0 1 4 3 2 1 1 3 1 2 1 " \
                             "3 1 2 1 2 1 1 1 2 3 2 1 1 0 1 1 3 2 1 2 6 2 1 1 " \
                             "1 2 3 3 3 2 3 0 3 2 1 1 0 0 1 4 3 0 1 5 0 2 0 1 " \
                             "2 1 3 0 1 2 2 1 1 0 3 0 0 4 5 0 3 0 2 1 1 3 0 3 " \
                             "2 2 1 1 0 2 1 0 2 2 1 2 0 2 2 5 2 2 1 1 2 1 2 2 " \
                             "2 2 1 1 3 4 0 2 1 1 0 1 2 2 1 1 1 5 2 0 3 2 1 1 " \
                             "2 2 3 0 3 0 1 3 1 2 3 0 2 1 2 2 1 2 3 0 1 2 3 1 " \
                             "1 3 1 0 1 1 3 0 2 1 2 2 0 2 1 1\n"

        # make sure solution matches computed result
        self.assertEqual(solution_raw, kmer_composition_raw)
        self.assertEqual(solution_formatted, kmer_composition_formatted)

    def test_kmer_positive_b(self):
        kmer_data = parse_gc_data("rosalind_kmer_2.txt")
        kmer_composition_raw = kmer(kmer_data, kmer_num)
        kmer_composition_formatted = format_output(kmer_composition_raw)

        solution_raw = {'AAAA': 389, 'AAAC': 392, 'AAAG': 356, 'AAAT': 365,
                        'AACA': 401, 'AACC': 402, 'AACG': 358, 'AACT': 414,
                        'AAGA': 387, 'AAGC': 391, 'AAGG': 400, 'AAGT': 394,
                        'AATA': 386, 'AATC': 364, 'AATG': 356, 'AATT': 399,
                        'ACAA': 380, 'ACAC': 421, 'ACAG': 432, 'ACAT': 389,
                        'ACCA': 390, 'ACCC': 406, 'ACCG': 428, 'ACCT': 407,
                        'ACGA': 354, 'ACGC': 376, 'ACGG': 363, 'ACGT': 400,
                        'ACTA': 385, 'ACTC': 358, 'ACTG': 420, 'ACTT': 412,
                        'AGAA': 347, 'AGAC': 435, 'AGAG': 421, 'AGAT': 435,
                        'AGCA': 393, 'AGCC': 379, 'AGCG': 387, 'AGCT': 379,
                        'AGGA': 395, 'AGGC': 390, 'AGGG': 373, 'AGGT': 400,
                        'AGTA': 402, 'AGTC': 396, 'AGTG': 408, 'AGTT': 407,
                        'ATAA': 386, 'ATAC': 399, 'ATAG': 406, 'ATAT': 374,
                        'ATCA': 367, 'ATCC': 382, 'ATCG': 385, 'ATCT': 395,
                        'ATGA': 355, 'ATGC': 392, 'ATGG': 390, 'ATGT': 376,
                        'ATTA': 421, 'ATTC': 396, 'ATTG': 398, 'ATTT': 338,
                        'CAAA': 416, 'CAAC': 404, 'CAAG': 392, 'CAAT': 371,
                        'CACA': 414, 'CACC': 414, 'CACG': 394, 'CACT': 374,
                        'CAGA': 411, 'CAGC': 370, 'CAGG': 369, 'CAGT': 407,
                        'CATA': 406, 'CATC': 374, 'CATG': 374, 'CATT': 405,
                        'CCAA': 424, 'CCAC': 373, 'CCAG': 389, 'CCAT': 388,
                        'CCCA': 370, 'CCCC': 347, 'CCCG': 380, 'CCCT': 378,
                        'CCGA': 425, 'CCGC': 394, 'CCGG': 377, 'CCGT': 396,
                        'CCTA': 391, 'CCTC': 389, 'CCTG': 388, 'CCTT': 380,
                        'CGAA': 379, 'CGAC': 378, 'CGAG': 373, 'CGAT': 379,
                        'CGCA': 380, 'CGCC': 413, 'CGCG': 371, 'CGCT': 388,
                        'CGGA': 382, 'CGGC': 363, 'CGGG': 378, 'CGGT': 371,
                        'CGTA': 391, 'CGTC': 412, 'CGTG': 419, 'CGTT': 384,
                        'CTAA': 413, 'CTAC': 383, 'CTAG': 398, 'CTAT': 389,
                        'CTCA': 388, 'CTCC': 385, 'CTCG': 391, 'CTCT': 371,
                        'CTGA': 373, 'CTGC': 359, 'CTGG': 368, 'CTGT': 423,
                        'CTTA': 391, 'CTTC': 435, 'CTTG': 390, 'CTTT': 380,
                        'GAAA': 341, 'GAAC': 390, 'GAAG': 396, 'GAAT': 365,
                        'GACA': 389, 'GACC': 411, 'GACG': 363, 'GACT': 381,
                        'GAGA': 422, 'GAGC': 375, 'GAGG': 404, 'GAGT': 393,
                        'GATA': 407, 'GATC': 427, 'GATG': 384, 'GATT': 367,
                        'GCAA': 367, 'GCAC': 399, 'GCAG': 376, 'GCAT': 395,
                        'GCCA': 410, 'GCCC': 359, 'GCCG': 400, 'GCCT': 389,
                        'GCGA': 355, 'GCGC': 384, 'GCGG': 355, 'GCGT': 384,
                        'GCTA': 416, 'GCTC': 391, 'GCTG': 371, 'GCTT': 393,
                        'GGAA': 394, 'GGAC': 372, 'GGAG': 400, 'GGAT': 392,
                        'GGCA': 375, 'GGCC': 385, 'GGCG': 349, 'GGCT': 415,
                        'GGGA': 392, 'GGGC': 360, 'GGGG': 350, 'GGGT': 363,
                        'GGTA': 385, 'GGTC': 380, 'GGTG': 355, 'GGTT': 395,
                        'GTAA': 403, 'GTAC': 408, 'GTAG': 406, 'GTAT': 367,
                        'GTCA': 384, 'GTCC': 389, 'GTCG': 413, 'GTCT': 405,
                        'GTGA': 389, 'GTGC': 394, 'GTGG': 378, 'GTGT': 401,
                        'GTTA': 411, 'GTTC': 386, 'GTTG': 406, 'GTTT': 394,
                        'TAAA': 356, 'TAAC': 389, 'TAAG': 428, 'TAAT': 404,
                        'TACA': 418, 'TACC': 404, 'TACG': 378, 'TACT': 406,
                        'TAGA': 418, 'TAGC': 402, 'TAGG': 385, 'TAGT': 419,
                        'TATA': 366, 'TATC': 364, 'TATG': 398, 'TATT': 382,
                        'TCAA': 412, 'TCAC': 403, 'TCAG': 360, 'TCAT': 387,
                        'TCCA': 404, 'TCCC': 363, 'TCCG': 384, 'TCCT': 374,
                        'TCGA': 375, 'TCGC': 398, 'TCGG': 399, 'TCGT': 426,
                        'TCTA': 391, 'TCTC': 397, 'TCTG': 344, 'TCTT': 411,
                        'TGAA': 372, 'TGAC': 359, 'TGAG': 400, 'TGAT': 379,
                        'TGCA': 389, 'TGCC': 382, 'TGCG': 371, 'TGCT': 389,
                        'TGGA': 389, 'TGGC': 411, 'TGGG': 364, 'TGGT': 381,
                        'TGTA': 406, 'TGTC': 403, 'TGTG': 380, 'TGTT': 411,
                        'TTAA': 375, 'TTAC': 416, 'TTAG': 414, 'TTAT': 380,
                        'TTCA': 423, 'TTCC': 369, 'TTCG': 409, 'TTCT': 372,
                        'TTGA': 393, 'TTGC': 386, 'TTGG': 409, 'TTGT': 400,
                        'TTTA': 362, 'TTTC': 356, 'TTTG': 394, 'TTTT': 341}

        solution_formatted = "389 392 356 365 401 402 358 414 387 391 400 394 " \
                             "386 364 356 399 380 421 432 389 390 406 428 407 " \
                             "354 376 363 400 385 358 420 412 347 435 421 435 " \
                             "393 379 387 379 395 390 373 400 402 396 408 407 " \
                             "386 399 406 374 367 382 385 395 355 392 390 376 " \
                             "421 396 398 338 416 404 392 371 414 414 394 374 " \
                             "411 370 369 407 406 374 374 405 424 373 389 388 " \
                             "370 347 380 378 425 394 377 396 391 389 388 380 " \
                             "379 378 373 379 380 413 371 388 382 363 378 371 " \
                             "391 412 419 384 413 383 398 389 388 385 391 371 " \
                             "373 359 368 423 391 435 390 380 341 390 396 365 " \
                             "389 411 363 381 422 375 404 393 407 427 384 367 " \
                             "367 399 376 395 410 359 400 389 355 384 355 384 " \
                             "416 391 371 393 394 372 400 392 375 385 349 415 " \
                             "392 360 350 363 385 380 355 395 403 408 406 367 " \
                             "384 389 413 405 389 394 378 401 411 386 406 394 " \
                             "356 389 428 404 418 404 378 406 418 402 385 419 " \
                             "366 364 398 382 412 403 360 387 404 363 384 374 " \
                             "375 398 399 426 391 397 344 411 372 359 400 379 " \
                             "389 382 371 389 389 411 364 381 406 403 380 411 " \
                             "375 416 414 380 423 369 409 372 393 386 409 400 " \
                             "362 356 394 341\n"

        # make sure solution matches computed result
        self.assertEqual(solution_raw, kmer_composition_raw)
        self.assertEqual(solution_formatted, kmer_composition_formatted)

    def test_kmer_positive_c(self):
        kmer_data = parse_gc_data("rosalind_kmer_3.txt")
        kmer_composition_raw = kmer(kmer_data, kmer_num)
        kmer_composition_formatted = format_output(kmer_composition_raw)

        solution_raw = {'AAAA': 315, 'AAAC': 331, 'AAAG': 278, 'AAAT': 364,
                        'AACA': 341, 'AACC': 327, 'AACG': 299, 'AACT': 309,
                        'AAGA': 323, 'AAGC': 316, 'AAGG': 300, 'AAGT': 306,
                        'AATA': 367, 'AATC': 331, 'AATG': 331, 'AATT': 360,
                        'ACAA': 334, 'ACAC': 312, 'ACAG': 342, 'ACAT': 337,
                        'ACCA': 324, 'ACCC': 288, 'ACCG': 323, 'ACCT': 337,
                        'ACGA': 316, 'ACGC': 322, 'ACGG': 293, 'ACGT': 328,
                        'ACTA': 316, 'ACTC': 324, 'ACTG': 310, 'ACTT': 313,
                        'AGAA': 325, 'AGAC': 301, 'AGAG': 324, 'AGAT': 298,
                        'AGCA': 322, 'AGCC': 322, 'AGCG': 322, 'AGCT': 301,
                        'AGGA': 333, 'AGGC': 340, 'AGGG': 306, 'AGGT': 307,
                        'AGTA': 320, 'AGTC': 312, 'AGTG': 337, 'AGTT': 368,
                        'ATAA': 318, 'ATAC': 341, 'ATAG': 339, 'ATAT': 341,
                        'ATCA': 348, 'ATCC': 328, 'ATCG': 340, 'ATCT': 336,
                        'ATGA': 320, 'ATGC': 331, 'ATGG': 359, 'ATGT': 353,
                        'ATTA': 324, 'ATTC': 330, 'ATTG': 343, 'ATTT': 331,
                        'CAAA': 324, 'CAAC': 308, 'CAAG': 313, 'CAAT': 378,
                        'CACA': 324, 'CACC': 323, 'CACG': 311, 'CACT': 319,
                        'CAGA': 305, 'CAGC': 321, 'CAGG': 347, 'CAGT': 347,
                        'CATA': 339, 'CATC': 355, 'CATG': 334, 'CATT': 318,
                        'CCAA': 310, 'CCAC': 317, 'CCAG': 322, 'CCAT': 321,
                        'CCCA': 319, 'CCCC': 309, 'CCCG': 305, 'CCCT': 332,
                        'CCGA': 342, 'CCGC': 331, 'CCGG': 297, 'CCGT': 335,
                        'CCTA': 326, 'CCTC': 333, 'CCTG': 314, 'CCTT': 334,
                        'CGAA': 335, 'CGAC': 310, 'CGAG': 334, 'CGAT': 336,
                        'CGCA': 318, 'CGCC': 307, 'CGCG': 321, 'CGCT': 316,
                        'CGGA': 308, 'CGGC': 330, 'CGGG': 312, 'CGGT': 311,
                        'CGTA': 326, 'CGTC': 331, 'CGTG': 326, 'CGTT': 328,
                        'CTAA': 331, 'CTAC': 310, 'CTAG': 305, 'CTAT': 333,
                        'CTCA': 330, 'CTCC': 322, 'CTCG': 325, 'CTCT': 308,
                        'CTGA': 323, 'CTGC': 313, 'CTGG': 332, 'CTGT': 324,
                        'CTTA': 309, 'CTTC': 338, 'CTTG': 315, 'CTTT': 327,
                        'GAAA': 329, 'GAAC': 335, 'GAAG': 320, 'GAAT': 318,
                        'GACA': 341, 'GACC': 297, 'GACG': 317, 'GACT': 303,
                        'GAGA': 299, 'GAGC': 338, 'GAGG': 336, 'GAGT': 323,
                        'GATA': 322, 'GATC': 352, 'GATG': 343, 'GATT': 305,
                        'GCAA': 340, 'GCAC': 315, 'GCAG': 349, 'GCAT': 340,
                        'GCCA': 297, 'GCCC': 333, 'GCCG': 319, 'GCCT': 326,
                        'GCGA': 318, 'GCGC': 298, 'GCGG': 333, 'GCGT': 319,
                        'GCTA': 321, 'GCTC': 324, 'GCTG': 334, 'GCTT': 303,
                        'GGAA': 311, 'GGAC': 320, 'GGAG': 304, 'GGAT': 337,
                        'GGCA': 367, 'GGCC': 315, 'GGCG': 301, 'GGCT': 350,
                        'GGGA': 293, 'GGGC': 327, 'GGGG': 300, 'GGGT': 328,
                        'GGTA': 319, 'GGTC': 317, 'GGTG': 329, 'GGTT': 343,
                        'GTAA': 321, 'GTAC': 324, 'GTAG': 308, 'GTAT': 323,
                        'GTCA': 301, 'GTCC': 348, 'GTCG': 312, 'GTCT': 315,
                        'GTGA': 352, 'GTGC': 343, 'GTGG': 364, 'GTGT': 297,
                        'GTTA': 349, 'GTTC': 364, 'GTTG': 316, 'GTTT': 327,
                        'TAAA': 320, 'TAAC': 302, 'TAAG': 334, 'TAAT': 329,
                        'TACA': 319, 'TACC': 325, 'TACG': 332, 'TACT': 332,
                        'TAGA': 321, 'TAGC': 292, 'TAGG': 303, 'TAGT': 361,
                        'TATA': 311, 'TATC': 314, 'TATG': 355, 'TATT': 345,
                        'TCAA': 339, 'TCAC': 333, 'TCAG': 307, 'TCAT': 348,
                        'TCCA': 330, 'TCCC': 335, 'TCCG': 358, 'TCCT': 312,
                        'TCGA': 339, 'TCGC': 311, 'TCGG': 338, 'TCGT': 329,
                        'TCTA': 316, 'TCTC': 304, 'TCTG': 334, 'TCTT': 338,
                        'TGAA': 332, 'TGAC': 327, 'TGAG': 334, 'TGAT': 351,
                        'TGCA': 337, 'TGCC': 331, 'TGCG': 324, 'TGCT': 315,
                        'TGGA': 338, 'TGGC': 336, 'TGGG': 330, 'TGGT': 362,
                        'TGTA': 311, 'TGTC': 316, 'TGTG': 364, 'TGTT': 317,
                        'TTAA': 315, 'TTAC': 333, 'TTAG': 325, 'TTAT': 328,
                        'TTCA': 348, 'TTCC': 337, 'TTCG': 340, 'TTCT': 333,
                        'TTGA': 349, 'TTGC': 320, 'TTGG': 311, 'TTGT': 334,
                        'TTTA': 319, 'TTTC': 326, 'TTTG': 340, 'TTTT': 319}

        solution_formatted = "315 331 278 364 341 327 299 309 323 316 300 306 " \
                             "367 331 331 360 334 312 342 337 324 288 323 337 " \
                             "316 322 293 328 316 324 310 313 325 301 324 298 " \
                             "322 322 322 301 333 340 306 307 320 312 337 368 " \
                             "318 341 339 341 348 328 340 336 320 331 359 353 " \
                             "324 330 343 331 324 308 313 378 324 323 311 319 " \
                             "305 321 347 347 339 355 334 318 310 317 322 321 " \
                             "319 309 305 332 342 331 297 335 326 333 314 334 " \
                             "335 310 334 336 318 307 321 316 308 330 312 311 " \
                             "326 331 326 328 331 310 305 333 330 322 325 308 " \
                             "323 313 332 324 309 338 315 327 329 335 320 318 " \
                             "341 297 317 303 299 338 336 323 322 352 343 305 " \
                             "340 315 349 340 297 333 319 326 318 298 333 319 " \
                             "321 324 334 303 311 320 304 337 367 315 301 350 " \
                             "293 327 300 328 319 317 329 343 321 324 308 323 " \
                             "301 348 312 315 352 343 364 297 349 364 316 327 " \
                             "320 302 334 329 319 325 332 332 321 292 303 361 " \
                             "311 314 355 345 339 333 307 348 330 335 358 312 " \
                             "339 311 338 329 316 304 334 338 332 327 334 351 " \
                             "337 331 324 315 338 336 330 362 311 316 364 317 " \
                             "315 333 325 328 348 337 340 333 349 320 311 334 " \
                             "319 326 340 319\n"

        # make sure solution matches computed result
        self.assertEqual(solution_raw, kmer_composition_raw)
        self.assertEqual(solution_formatted, kmer_composition_formatted)

    def test_kmer_negative(self):
        kmer_data = parse_gc_data("rosalind_kmer_4.txt")
        kmer_composition_raw = kmer(kmer_data, kmer_num)
        kmer_composition_formatted = format_output(kmer_composition_raw)

        solution_raw = {}

        solution_formatted = ""

        # make sure solution matches computed result
        self.assertEqual(solution_raw, kmer_composition_raw)
        self.assertEqual(solution_formatted, kmer_composition_formatted)


if __name__ == '__main__':
    unittest.main()
