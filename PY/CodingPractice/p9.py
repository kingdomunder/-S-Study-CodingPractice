# 9. 직사각형 별찍기 / 가로길이 n , 세로길이 m 

n = 2
m = 5

def Solution(h,v):    
    for i in range(v):
        print("*" * h)        
    
Solution(n,m)


# 기준 형식대로 풀어보기

# a, b = map(int, input().strip().split(' '))
# print(a + b)
