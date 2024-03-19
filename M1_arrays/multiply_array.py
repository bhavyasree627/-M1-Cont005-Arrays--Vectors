"""
Intuition:

The function multiply(arr) takes an array of numbers arr as input.
It aims to calculate the product (multiplication) of all the elements in the array.
Approach:

Initialization:

A variable pro is created and initialized to 1. This will act as an accumulator to store the product as elements are multiplied.
Iteration:

A for loop iterates through each element i in the array arr.
Multiplication:

Inside the loop, the current element i is multiplied with the current value of pro. This essentially accumulates the product of all elements encountered so far.
The result is stored back into pro.
Main Loop:

The code takes an integer input t representing the number of test cases.
For each test case:
It reads the number of elements n in the array.
It creates an array arr by reading n integers from the input, converting them to integers using map(int, input().split()).
It calls the multiply(arr) function (assuming it returns the product).
"""
def multiply(arr):
    pro=1
    for i in arr:
        pro*=i
    print(pro)
    return

t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    multiply(arr)