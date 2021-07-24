list = [6,8,3,9,10,1,2,4,7,5]

def divide(A,g1,g2):
    for x in range(0,int(len(A)/2)):
        g1.append(A[x])
    for x in range (int(len(A)/2),len(A)):
        g2.append(A[x])

def Sort(group,sorted):
    sorted.insert(0, group[0])
    group.pop(0)
    indexNo = len(sorted)
    while len(group) != 0:
        if group[0] > sorted[indexNo-1]:
            sorted.insert(indexNo,group[0])
            group.pop(0)
            indexNo = len(sorted)
            continue
        elif indexNo == 1:
            sorted.insert(0,group[0])
            group.pop(0)
            indexNo = len(sorted)
            continue
        else:
            indexNo -= 1 

def MergeSort(LIST):
    g1=[]
    g2=[]

    divide(LIST,g1,g2)
    
    g1sorted = []
    g2sorted = []

    Sort(g1,g1sorted)
    Sort(g2,g2sorted)
    
    result=[]

    while len(g1sorted) and len(g2sorted) != 0:
        if g1sorted[0] < g2sorted[0]:
            result.append(g1sorted[0])
            g1sorted.pop(0)
        elif g1sorted[0] > g2sorted[0]:
            result.append(g2sorted[0])
            g2sorted.pop(0)
    
    result = result + g1sorted
    result = result + g2sorted

    return result

print(MergeSort(list))







