x, n = map(int, input().split())
p = set(map(int, input().split()))

for i in range(110):
    if x - i not in p:
        print(x - i)
        break
    elif x + i not in p:
        print(x + i)
        break