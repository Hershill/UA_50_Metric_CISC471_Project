def files():
    DNAlist = []
    file1 = open('DNA.txt', 'r')
    Lines = file1.readlines()     
    for line in Lines:
        DNAlist.append(line.strip())
    return DNAlist


def grouping(DnaList):
    longest_string = max(DnaList, key=len)
    Storage = []
    for i in DnaList:
        checker = 0
        j = len(Storage)
        while j > 0:
            if Storage[len(Storage) - j][0] == len(i):
                checker = 1
                position = len(Storage) - j
            j -= 1
        if checker == 1:
            Storage[position][1] += 1
        else:
            temp = [len(i), 1]
            Storage.append(temp)
    return Storage

def calculator(Array, percent):
    Sum = 0
    for i in Array:
        j = Array.index(i)
        Sum += Array[j][0] * Array[j][1]
    percentSum = Sum * percent
    Array = Sort(Array)
    while percentSum > 0:
        for i in reversed(Array):
            j = Array.index(i)
            while Array[j][1] > 0:
                if (percentSum - Array[j][0]) <= 0:
                    return Array[j][0]
                else:
                    percentSum -= Array[j][0]
                    Array[j][1] -= 1
    

def Sort(Array): 
    return(sorted(Array, key = lambda x: x[0]))

def Reverse(Array):
    Array1 = []
            
def main():
    Array = grouping(files())
    number = calculator(Array,.5)
    print("N50" + number)
    number2 = calculator(Array,.75)
    print("N75" + number2)

main()
