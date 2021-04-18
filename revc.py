from parsers import *

def revc(dna):
  '''
  Returns the reverse complement of a given DNA string of length at most 1000bp
  '''
  rev_complement = ""
  reversed_dna = dna[::-1]

  for n in reversed_dna:
    if n == "A":
      rev_complement = rev_complement + "T"
    elif n == "T":
      rev_complement = rev_complement + "A"
    elif n == "G":
      rev_complement = rev_complement + "C"
    elif n == "C":
      rev_complement = rev_complement + "G"
  return rev_complement


if __name__ == '__main__':
    # filename = "dna_sample_data.txt"
    filename = "rosalind_revc.txt"
    dna_str = parse_dna_data(filename)
    print(dna_str)
    rev_complement = revc(dna_str)
    print(rev_complement)