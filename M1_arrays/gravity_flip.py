"""
1. Take input of size of array and then the array.
2. Then gravity influence here is nothing but start regions should have less blocks.
3. Accordingly just return or print the sorted array.
"""
n=int(input())
array=list(map(int,input().split()))
print(*sorted(array))
