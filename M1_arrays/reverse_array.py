"""
Intuition: 
Traverse from front of the array and rear of the array and swap the elements till mid.
Approach:
1) Traverse from both ends towards the middle.
2) Write a function and pass the array the start index(0) and end_index(n-1)
3) If start_index < less_index then we did not reach mid yet.
4) Swap the elements at start_index and end_index in the array. 
5) Recursively call the function with start_index+1 and _end_index-1.
6) Base case is when start_index > end_index, which means we have reached the mid point,then return the array.
Time Complexity: O(n)
Space Complexity: O(1) for iterative approach, O(n) for recursive approach.
"""
# RECURSIVE APPROACH
def reverse(arr,i,j):
    if i<j:
        #swap
        arr[i],arr[j] = arr[j],arr[i]
        i+=1
        j-=1
        return reverse(arr,i,j)
    return arr
n=int(input())
array=list(map(int,input().split()))
reversed_array=reverse(array,0,n-1)
print(*reversed_array)

# ITERATIVE APPROACH
def reverse_iterative(arr):
    n = len(arr)
    for i in range(n // 2):
        arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]
    return arr
n=int(input())
array=list(map(int,input().split()))
reversed_array=reverse(array)
print(*reversed_array)