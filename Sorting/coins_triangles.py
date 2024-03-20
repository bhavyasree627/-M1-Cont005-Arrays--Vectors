def max_triangle_height(N):
    height = 1
    while (height * (height + 1)) // 2 <= N:
        height += 1
    return height - 1
T = int(input())
for _ in range(T):
    N = int(input())
    print(max_triangle_height(N))
