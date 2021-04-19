from algorithms import nxx, uxx, ugxx, lxx
from sample_data_generator import count_contig_pct

def output_scores(dna_set, pct, ref_genome):
  """Return metrics for assembly: NXX, UXX, UGXX and L50 and dna set composition

  :param dna_set: list of DNA contigs
  :param pct: percentage threshold for UG score
  :param ref_genome: reference genome
  :param percentage: tuple containg scores for NXX, UXX, UGXX and L50 dna set composition %
  """
  n50 = nxx(dna_set,pct)
  u50 = uxx(dna_set, pct, ref_genome)
  ug50 = ugxx(dna_set, pct, ref_genome)
  l50 = lxx(dna_set,pct)
  composition = count_contig_pct(dna_set) # percent composition of short, medium and long contigs

  return n50, u50, ug50, l50, composition

