def wins(a,b,n):
    i,j=0,0
    count=0
    while i<n:
        if a[i]>b[j]:
            count+=1
            i+=1
            j+=1
        else:
            i+=1
    return count
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    a.sort()
    b.sort()
    print(wins(a,b,n))