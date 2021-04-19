from parsers import *

def iprb(k,m,n):
  k = int(k)
  m = int(m)
  n = int(n)
  total = k+m+n
  DD = k/total * ((k-1)/(total-1))*1 + k/total * (m/(total-1))*1 + k/total * (n/(total-1))*1
  Dd = m/total * (k/(total-1))*1 + m/total * ((m-1)/(total-1))*(3/4) + m/total * (n/(total-1))*(2/4)
  dd = n/total * (k/(total-1))*1 + n/total * (m/(total-1))*(2/4) + n/total * ((n-1)/(total-1))*0
  prob = round(DD + Dd + dd, 5)
  
  return prob




if __name__ == '__main__':
  # filename = "hamm_sample_data.txt"
  filename = "rosalind_iprb.txt"
  kmn = parse_iprb_data(filename)
  print(kmn)
  prob = iprb(kmn[0],kmn[1],kmn[2])
  print(prob)