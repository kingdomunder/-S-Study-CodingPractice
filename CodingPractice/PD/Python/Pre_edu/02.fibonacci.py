list = [1,1]


def A(n):
    list.append(list[n-3]+list[n-2])



def fibonacci(n):
    for x in range(3,n+1):
        A(x)


    return list[n-1]




print(fibonacci(int(input("숫자 입력 : "))))