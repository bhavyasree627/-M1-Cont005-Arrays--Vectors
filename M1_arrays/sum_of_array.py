"""
Imagine you have a basket of items, and you want to find the total weight of all the items combined. This code acts like a weighing scale:
It starts with an empty scale (s = 0).
It iterates through each item in the basket (for i in array).
For each item, it places it on the scale and adds its weight to the running total (s += i).
After processing all items, the final value of s represents the total weight of everything in the basket (the sum of all elements in the array).
"""
def sum_of_all_elements(array):
    s=0
    for i in array:
        s+=i
    return s 
t=int(input())
for i in range(t):
    n=int(input())
    array=list(map(int,input().split()))
    print(sum_of_all_elements(array))