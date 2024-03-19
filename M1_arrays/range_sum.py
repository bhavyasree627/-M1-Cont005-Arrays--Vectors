#Range Sum

n, q = map(int, input().split())
l = list(map(int, input().split()))
prefix_sums = [0] * (n + 1)
for i in range(1, n + 1):
    prefix_sums[i] = prefix_sums[i - 1] + l[i - 1]
while q:
    L, R = map(int, input().split())
    s = prefix_sums[R] - prefix_sums[L - 1]
    print(s)
    q -= 1