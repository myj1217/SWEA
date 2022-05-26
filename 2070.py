# 2070. 큰 놈, 작은 놈, 같은 놈

for tc in range(int(input())):
    a,b = map(int, input().split())
    print("#{} ".format(tc+1), end="")
    if a == b:
        print("=")
    elif a > b:
        print(">")
    else:
        print("<")