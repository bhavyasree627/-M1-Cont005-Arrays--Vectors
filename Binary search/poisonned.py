def erfen(x,lst):
    l=0
    r=len(lst)-1
    while l<r:
        mid=(l+r)//2
        if lst[mid]<x:
            l=mid+1
        else:
            r=mid
    return l

n=int(input())
lst=list(map(int,input().split()))
lst1=[0 for i in range(n)]
for i in range(n):
    if i==0:
        lst1[i]=lst[i]
    else:
        lst1[i]=lst1[i-1]+lst[i]
m=int(input())
lst2=list(map(int,input().split()))
for i in lst2:
    result=erfen(i,lst1)
    print(result+1)

		   	 		  	 			 		 		   			 	