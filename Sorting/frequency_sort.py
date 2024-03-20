import heapq
t=int(input())
for _ in range(t):
    n=int(input())
    li=list(map(int,input().split()))
    ans=[]
    heap=[]
    hash={}
    for i in li:
        if i in hash:
            hash[i]+=1
        else:
            hash[i]=1
    for i in hash.keys():
        heapq.heappush(heap,(hash[i],i))
    while heap:
        pop=heapq.heappop(heap)
        for i in range(pop[0]):
            ans.append(pop[1])
    print(*ans)