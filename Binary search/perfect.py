q = int(input())
for _ in range(q):
    c, m, x = map(int, input().split())
    if c == 0 or m == 0:
        print(0)
    else:
        total = (c + m + x) // 3
        print(min(c, m, total))