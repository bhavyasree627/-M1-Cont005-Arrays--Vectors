"""
1. Take the inputs and create a function.
2. In the function initialize a hashmap.
3. Iterate through the array and add up the non existent elements in hashmap to it.
4. If the element is already in the hashmap, it simply means repetition.
5. Stop and return that duplicated element.
6. Return -1 if there are no duplicates.
"""
def find_duplicate(arr):
    hash={}
    for i in arr:
        if i not in hash:
            hash[i]=1
        else:
            return i
    return -1
n=int(input())
array=list(map(int,input().split()))
print(find_duplicate(array))