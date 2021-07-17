# 선택정렬(자리에 값을 선택)   /  버블정렬(인접 두자료 비교)  /  삽입정렬(값을 선택한 자리에)
# [9, 4, 3, 1, 12]을 오름차순 정렬

a = [9, 4, 3, 1, 12]


for y in range(len(a)-1):

    for x in a:
        if a.index(x) > len(a)-2:
            break
        elif x > a[a.index(x) + 1]:
            a.insert(a.index(x),a[a.index(x)+1])
            a.pop(a.index(x)+1)

Min = a[0]

print(a)

print(Min)
