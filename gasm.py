from revc import revc
from parsers import parse_gasm_data

def gasm(dna):
  l = len(dna[0])
  
  for k in range(l-1,1,-1):
    adj = get_adj(dna,l,k)
    first = kmer = next(iter(adj))
    superstring = ''
    
    while True:
      if kmer in adj:
        cyclic_superstring += kmer[-1]
        kmer = adj.pop(kmer)
        if kmer == first:
          return cyclic_superstring
      else:
          break

def get_adj(dna,length,k):
  adj = dict()
  for d in dna:
    for i in range(length-k):
      adj[d[i:i+k]] = d[i+1:i+k+1]
  return adj

if __name__ == '__main__':
  dna = parse_gasm_data("rosalind_gasm.txt")
  dna = list(set(dna + [revc(i) for i in dna]))
  print(dna)

  cyclic_superstring = gasm(dna)
  print(cyclic_superstring)