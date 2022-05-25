# 2063. 중간값 찾기

n = int(input())
data = list(map(int, input().split()))

data.sort()
medi = n // 2
print(data[medi])