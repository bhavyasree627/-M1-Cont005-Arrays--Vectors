def repeated(arr):
    hash={}
    res=[]
    for i in arr:
        if i not in hash:
            hash[i]=1
        else:
            hash[i]+=1
    for i in hash.keys():
        if hash[i]>1:
            res.append(i)
    return res
t=int(input())
for i in range(t):
    n=int(input())
    array=list(map(int,input().split()))
    ans=repeated(array)
    print(*ans)
