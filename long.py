from parsers import *

def long(FASTA_sets):
  pairs = {}
  superstring = ""
  for dna_name in FASTA_sets:
    pairs[(FASTA_sets[dna_name])] = [0,""]
  
  

  while len(pairs.keys()) > 1:
    for dna1 in pairs:
      for dna2 in pairs:
        if dna1 != dna2:
          lcs = longestCommonSequence(dna1,dna2)
          if len(lcs) > pairs[dna1][0]:
            pairs[dna1] = [len(lcs), dna2]
          elif len(lcs) == pairs[dna1][0]:
            pairs[dna1].append(dna2)
    pairs = find_pair(pairs)
  
  superstring = list(pairs.keys())[0]

  return superstring

def find_pair(pairs):
  for dna1 in pairs:
    for dna2 in pairs:
      if dna1 != dna2:
        if dna1 in pairs[dna2] and pairs[dna2][0] > pairs[dna1][0]:
          pairs[merge(dna2,dna1)] = [0,""]
          pairs.pop(dna1)
          pairs.pop(dna2)
          return pairs
        else:
          pairs[merge(dna1,dna2)] = [0,""]
          pairs.pop(dna1)
          pairs.pop(dna2)
          return pairs

def merge(a, b):
  max_offset = len(b)  # can't overlap with greater size than len(b)
  for i in reversed(range(max_offset+1)):
    # checks for equivalence of decreasing sized slices
    if a[-i:] == b[:i]:
      break
  return a + b[i:]

def longestCommonSequence(string1, string2):
  answer = ""
  len1, len2 = len(string1), len(string2)
  for i in range(len1):
    match = ""
    for j in range(len2):
      if (i + j < len1 and string1[i + j] == string2[j]):
        match += string2[j]
      else:
        if (len(match) > len(answer)): answer = match
        match = ""
  return answer

if __name__ == '__main__':
  filename = "rosalind_long.txt"
  FASTA_data = parse_gc_data(filename)
  print(FASTA_data)
  superstring = long(FASTA_data)
  print(superstring)