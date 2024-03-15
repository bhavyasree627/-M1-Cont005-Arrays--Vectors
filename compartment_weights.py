"""
Intuition:
The code processes multiple test cases (t).
In each test case:
It reads the size of an array (n) and the array elements (arr).
It calculates the initial sum of all elements (ans).
It reads the number of queries (q).
For each query:
It retrieves the starting index (s), ending index (e), and weight (w) for a subarray update.
It efficiently updates the ans variable to account for the subarray modification without explicitly recalculating the entire sum from scratch.
Approach:
Input and Initialization:
The code takes the number of test cases (t) as input.
Inside a loop that iterates t times:
It reads the array size (n) and initializes the array (arr) with the input elements.
It sets the initial sum (ans) to 0.
Query Processing:
It reads the number of queries (q) for the current test case.
Inside a nested loop that iterates q times:
It reads the starting index (s), ending index (e), and weight (w) for the subarray update.
It leverages the concept of "frequency contribution":
Instead of recalculating the entire sum, it considers the contribution of each element in the subarray to the overall sum (ans).
For elements added (w), it adds their frequency (number of times included in the subarray based on e-s+1) multiplied by their weight (w).
For elements removed (weight becomes 0), it effectively subtracts their previous contribution (arr[i]).
Output:
After processing all queries, the final value of ans (representing the modified sum) is printed for the current test case.
"""
t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    ans=0
    for i in arr:
        ans+=i
    q=int(input())
    for _ in range(q):
        s,e,w=map(int,input().split())
        ans+=(e-s+1)*w
    print(ans)