from parsers import parse_gasm_data

def pcov(dna):
  l = len(dna[0])
  
  for k in range(l-1,1,-1):
    adj = get_adj(dna,l,k)
    first = kmer = next(iter(adj))
    superstring = ''
    
    while True:
      if kmer in adj:
        superstring += kmer[-1]
        kmer = adj.pop(kmer)
        if kmer == first:
          return superstring
      else:
          break

def get_adj(dna,length,k):
  adj = dict()
  for d in dna:
    for i in range(length-k):
      adj[d[i:i+k]] = d[i+1:i+k+1]
  return adj


if __name__ == '__main__':
  dna = parse_gasm_data("rosalind_pcov.txt")
  print(dna)

  superstring = pcov(dna)
  print(superstring)