list = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
    
def quick(a):
    if 0 == len(a): return []
  
    g1=[]
    g2=[]
    i = 0
    list_b = []
    pivot = a[len(a)-1]
  
    while i < len(a):
        if a[i] < pivot:
            g1.append(a[i])
        elif a[i] > pivot:
            g2.append(a[i])
        i = i + 1

    g1 = quick(g1)
    g2 = quick(g2)

    list_b.extend(g1)
    list_b.append(pivot)
    list_b.extend(g2)
  
    return list_b

print('list :',list)
print('sort list :',quick(list))