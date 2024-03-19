""" 
Assign the minimum value to our maximum to find the maximum.

1. Take integer and array inputs accordingly
2. Then initialize a maxi variable with the minimum value possible it can be arr[0] too.
3. Then iterate through the loop to find the maximum by comparing with the elements in the array.
4. print or return the maximum value 

Time Complexity - O(n)
Space Complexity - O(1)

"""
def maximum_element(arr):
    maxi=arr[0]
    for i in arr:
        if i>maxi:
            maxi=i
    return maxi

n=int(input())
arr=list(map(int,input().split()))
print(maximum_element(arr))
