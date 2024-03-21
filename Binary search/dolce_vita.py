T = int(input())

def solve(idx: int, limit: int, b) -> int:
    if b[idx] > limit:
        return 0
    l, r = 1, 10 ** 9
    while l <= r:
        mid = l + r >> 1
        if b[idx] + (idx + 1) * (mid - 1) <= limit:
            l = mid + 1
        else:
            r = mid - 1
    return r

for _ in range(T):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    b = a[:]
    for i in range(1, n):
        b[i] += b[i - 1]
    ans = 0
    for i in range(n):
        ans += solve(i, x, b)
    print(ans)

   				     		  	  				  				 	