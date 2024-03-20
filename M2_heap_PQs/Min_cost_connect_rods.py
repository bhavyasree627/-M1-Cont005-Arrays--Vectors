import heapq
def find_cost(arr):
    heapq.heapify(arr)
    ans=0
    while len(arr) > 1:
        small1=heapq.heappop(arr)
        small2=heapq.heappop(arr)
        merge=small1 + small2
        ans+=merge
        heapq.heappush(arr,merge)
    return ans

t=int(input())
for _ in range(t):
    n=int(input())
    li=list(map(int,input().split()))
    total=find_cost(li)
    print(total)