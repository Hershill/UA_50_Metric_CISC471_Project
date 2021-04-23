from parsers import *

def long(FASTA_sets):
    dna_set = list(FASTA_sets.values())
    superstring = find_superstring(dna_set)
    return superstring

def find_superstring(dna_set, dna=''):
    if (len(dna_set) == 0):
        return dna

    elif (len(dna) == 0):
        dna = dna_set.pop(0)
        return find_superstring(dna_set, dna)

    else:
        for i in range(len(dna_set)):
            dna1 = dna_set[i]
            for j in range(len(dna1) // 2):
                idx = len(dna1) - j
                if dna.startswith(dna1[j:]):
                    dna_set.pop(i)
                    return find_superstring(dna_set, dna1[:j] + dna)
                if dna.endswith(dna1[:idx]):
                    dna_set.pop(i)
                    return find_superstring(dna_set, dna + dna1[idx:])
                
if __name__ == '__main__':
    filename = "rosalind_long.txt"
    FASTA_data = parse_gc_data(filename)
    print(FASTA_data)
    superstring = long(FASTA_data)
    print(superstring)