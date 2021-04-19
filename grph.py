from parsers import *

def grph(FASTA_sets):
  """Return adjacency list corresponding to O3
  :param FASTA_sets: strings fo nucleotides
  :return: adjacent list corresponding to O3
  """
  dna_names = []
  dna_strings = []
  edges = []

  for dna_name in FASTA_sets:
    dna_names.append(dna_name)

  for dna_name in FASTA_sets:
    dna_strings.append(FASTA_sets[dna_name])
  
  for cur_dna in dna_strings:
    suffix = cur_dna[len(cur_dna)-3:]
    for dna1 in dna_strings:
      if dna1 != cur_dna:
        prefix = dna1[:3]
        if suffix == prefix:
          edge = (dna_names[dna_strings.index(cur_dna)],dna_names[dna_strings.index(dna1)])
          edges.append(edge)
  return edges
      
def format_output(edges):
  formatted_str = ""
  for edge in edges:
    formatted_str = formatted_str + f"{edge[0]} {edge[1]} \n" 
  return formatted_str

if __name__ == '__main__':
    filename = "rosalind_grph.txt"
    FASTA_data = parse_gc_data(filename)
    print(FASTA_data)
    adj_list = grph(FASTA_data)
    print(adj_list)
    formatted_str = format_output(adj_list)
    print(formatted_str)