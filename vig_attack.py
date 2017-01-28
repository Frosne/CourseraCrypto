
import vig
from sets import Set

def factor(n):
    a = Set()
    nh = n/2
    for i in range(2,nh+2):
        if (n%i == 0):
            a.add(i)
    return sorted(list(a))    

def kasinski(message):
    lst =  map(lambda x: bigram_treatment(x), generate_bigram(message))
    print(lst)
    dict = {}
    for i in lst:
        temp_lst = i[1::]
        for j in temp_lst:
            if not (j in dict):
                dict[j] = 1
            else:
                dict[j]=dict[j]+1
    return dict            


def bigram_treatment(lst_occ):
    a = Set()
    lst = map(lambda x: Set(factor(x)), lst_occ[1::])
    for i in lst:
        a = a | i
    return [lst_occ[0]] + list(a)    

def bigram_search(message, bigram):
    result = 0
    lst = [bigram]
    while (result !=-1):
        result = message.find(bigram, result+1)
        if not result == -1 :
            lst = lst + [result]

    lst_occ = [bigram]
    for i in range(1, len(lst)-1):
        val = (lst[i+1] - lst[i])
        if not (val in lst_occ):
            lst_occ = lst_occ+[val]
    if (len(lst_occ) == 1):
        return None        
    return lst_occ

def generate_bigram(message):
    bigrams = Set()
    result = []
    for i in range(0, len(message)-1):
        bigrams.add(message[i]+message[i+1])
    for i in bigrams:
        temp =  bigram_search(message, i)
        if (temp != None):
            result = result + [bigram_search(message, i)]
    return result    

def main():
    print(kasinski("abababhjhjab"))
    

if __name__ == '__main__':
    main()