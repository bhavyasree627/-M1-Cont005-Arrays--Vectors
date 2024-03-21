def main():
    t = int(input())  # Number of test cases
    for _ in range(t):
        count = 0
        n, k = map(int, input().split())  # Value of n and k for the current test case
        for f in range(n // 2 + 1):
            if check(f, n - f, k):  # Check if the pair satisfies the condition
                count += 1
        print(count)  # Print the count for the current test case
def check(f, g, k):
    for i in range(k - 3):
        temp = g - f
        g = f
        f = temp
        if g < f:  # Check if the pair satisfies the condition
            return False
    return True
if __name__ == "__main__":
    main()