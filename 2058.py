# 2058. 자릿수 더하기

result = 0
num = int(input())

while True:
    if num == 0:
        break
    result += num % 10
    num = num // 10

print(result)