def list_correlation(position, ciphered):
    d = text_pretreatment('./jane')
    r = list_treatment(lst)

def text_pretreatment(address):
    from collections import OrderedDict
    f = open(address,'r')
    c = f.read(1)
    dic = {}
    while  c:
        if c >= 'a' and c<='z':
            if c in dic:
                dic[c]+=1
            else:
                dic[c]=1
        c = f.read(1)        
    sum_ = float(sum(dic.values()))
    d =  dict(zip(dic.keys(), map(lambda x : round(round(float(x) / sum_,4) *100,2) , dic.values())))                
    return OrderedDict(sorted(d.items(), key=lambda t: t[1]))



def list_treatment(lst):
    dic = {}
    for i in lst:
        if not (i in dic):
            dic[i]=1
        else:
            dic[i]+=1

    dict2 = {}
    sum_ = float(sum(dic.values()))
    d =  dict(zip(dic.keys(), map(lambda x : round(float(x) / sum_,2) , dic.values())))
    return OrderedDict(sorted(d.items(), key=lambda t: t[1]))

def regenerate_text(message, key):
    lst = []
    for i in range(key):
        lst.append([])
    for i in range(len(message)):
        lst[i%key] = lst[i%key] + [message[i]]
    return lst    

def main():
    print(text_pretreatment('./jane'))
    """print(regenerate_text("mioutasasfasf",9))
    print(list_treatment(['a', 'b', 'a']))
"""

if __name__ == '__main__':
            main()       