"""
Intuition:
This code aims to identify and print the unique elements present in a given input array.
It iterates through the array, checking if the current element is different from the previous one.
If it's different, it's considered unique and printed.

Approach:
1. Base Case (Single Element):
If the array has only one element (len(arr) == 1), it's inherently unique, so all elements are printed using print(*arr).
2. Iterative Comparison (Multiple Elements):
The code iterates through the array using a for loop.
For the first element (i == 0), it's always printed since there's no previous element for comparison.
For subsequent elements (i > 0), it checks if the current element (arr[i]) is different from the previous element (arr[i-1]).
If they are different, the current element is considered unique and printed using print(arr[i], end=" ") with a space to separate elements.
3. Newline:
After iterating through the array, a newline character (print()) is used to move to the next line for the next test case.
"""
def unique(arr):
    if len(arr)==1:
        print(*arr)
    else:
        for i in range(len(arr)):
            if i==0:
                print(arr[i],end=' ')
            else:
                if arr[i]!=arr[i-1]:
                    print(arr[i],end=" ")
        print()
    return
t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    unique(arr)