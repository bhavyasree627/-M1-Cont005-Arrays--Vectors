"""
1. Take inputs and initialize an array.
2. Call a function for linear search to find the index of the number residence in the array.
3. Iterate with for loop using indices and return index once the number is found.
4. For being safe return -1
"""
def linear_search(arr,num):
    for i in range(len(arr)):
        if arr[i] == num:
            return i
    return -1
n,num=map(int,input().split())
array=list(map(int,input().split()))
print(linear_search(array,num))