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
Printing (Optional):

The code snippet you provided includes a print(pro) statement within the function. However, the function itself doesn't return anything. If you want to print the product outside the function, you'll need to remove this print statement and make the function return pro.
Return (Optional):

The provided code snippet doesn't explicitly return anything from the multiply function. If you want to use the product value in other parts of your code, you'll need to add a return pro statement at the end of the function.
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