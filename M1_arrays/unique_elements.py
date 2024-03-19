"""
1. Take inputs and call out for unique function that prints all unique elements.
2. Intialize a hashmap in the function.
3. Iterate through the array and add up the elements to hashmap like a counter
4. Finally traverse the hashmap and print the keys whose value corresponds to one
5. Just add up a return statements to maintain standards.
"""
def unique(array):
    s={}
    for i in array:
        if i not in s:
            s[i]=1
        else:
            s[i]+=1
    for i in s.keys():
        if s[i]==1:
            print(i,end=" ")
    return
n=int(input())
array=list(map(int,input().split()))
unique(array)