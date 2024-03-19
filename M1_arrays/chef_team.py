"""
Intuition:
The code checks if a given number n has the same number of even and odd divisors (including 1 and itself). If it does, it prints 1, otherwise, it prints 0.

Approach:
Initialization:
odd and even are initialized to 0 to count the number of odd and even divisors, respectively.
Looping through divisors:

A for loop iterates from 1 to n (inclusive) to check each potential divisor i of n.
Divisibility check:

The if statement checks if n is divisible by i using the modulo operator (%).
Counting even/odd divisors:

If n is divisible by i:
An inner if statement checks if i is even using the modulo operator (%).
If i is even, even is incremented.
If i is odd, odd is incremented.
Result determination:

After the loop completes, an if statement checks if odd is equal to even.
If they are equal, it means n has the same number of even and odd divisors, so it prints 1.
Otherwise, it prints 0.
Multiple test cases:

The code takes an integer t (number of test cases) as input using input().
A for loop iterates t times.
Inside the loop, an integer n is taken as input for each test case.
The chef(n) function is called to process each test case.
"""
def chef(n):
    odd=0
    even=0
    for i in range(1,n+1):
        if n%i==0:
            if i%2==0:
                even+=1
            else:
                odd+=1
    if odd==even:
        print(1)
    else:
        print(0)
    return

t=int(input())
for _ in range(t):
    n=int(input())
    chef(n)