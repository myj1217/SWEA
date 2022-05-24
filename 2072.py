# 2072. 홀수만 더하기

T = int(input())

for test_case in range(1, T + 1):
    data = list(map(int, input().split()))
    result = 0
    for j in range(len(data)) :
        if data[j] % 2 == 1 :
            result += data[j]

    print('#%d %d' % (test_case, result))