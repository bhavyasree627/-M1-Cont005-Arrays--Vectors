def solve(A, B, N, M, K):
    A.sort()
    B.sort()
    ptrA, ptrB, ans = 0, 0, 0
    while ptrA < N and ptrB < M:
        if abs(A[ptrA] - B[ptrB]) <= K:
            ans += 1
            ptrA += 1
            ptrB += 1
        elif A[ptrA] < B[ptrB]:
            ptrA += 1
        else:
            ptrB += 1
    return ans

n,m,k=map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
print(solve(a,b,n,m,k))