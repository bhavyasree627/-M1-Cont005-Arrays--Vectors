"""
1. Take the input of size of array and then the array.
2. Then create a function to calculate the sum of odd elements for organised code.
3. In the function iterate through the array and add up the sum of all odd elements.
4. Return the sum.
"""
def sum_of_odd(arr):
    s=0
    for i in arr:
        if i%2!=0:
            s+=i
    return s
n=int(input())
array=list(map(int,input().split()))
odd_sum = sum_of_odd(array)
print(odd_sum)