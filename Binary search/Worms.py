def binary_search(x, lst):
    l = 0
    r = len(lst) - 1
    while l < r:
        mid = (l + r) // 2
        if lst[mid] < x:
            l = mid + 1
        else:
            r = mid
    return l

# Input size of lst
n = int(input())

# Input elements of lst
lst = list(map(int, input().split()))

# Perform cumulative sum on lst to create lst1
lst1 = [0] * n
for i in range(n):
    if i == 0:
        lst1[i] = lst[i]
    else:
        lst1[i] = lst1[i - 1] + lst[i]

# Input size of lst2
m = int(input())

# Input elements of lst2
lst2 = list(map(int, input().split()))

# For each element in lst2, find insertion position in lst1 using binary search
for i in lst2:
    result = binary_search(i, lst1)
    print(result + 1)
