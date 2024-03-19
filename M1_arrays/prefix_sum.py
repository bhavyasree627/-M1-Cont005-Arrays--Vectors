import sys

class PrefixSum:
    def __init__(self):
        pass
    
    def calculate_prefix_sum(self):
        # Get the number of test cases
        num_test_cases = int(input())
        
        # Iterate over each test case
        for _ in range(num_test_cases):
            # Input size of array
            N = int(input())
            # Input array elements
            arr = list(map(int, input().split()))
            # Input number of queries
            Q = int(input())
            
            # Calculate prefix sum
            prefix_sum = [0] * (N + 1)
            prefix_sum[1] = arr[0]

            for i in range(2, N + 1):
                prefix_sum[i] = prefix_sum[i - 1] + arr[i - 1]
            
            # Answer queries
            for _ in range(Q):
                # Input query range
                L, R = map(int, sys.stdin.readline().split())
                # Calculate sum within range using prefix sum
                sum_range = prefix_sum[R] - prefix_sum[L - 1]
                print(sum_range)

# Create an instance of the PrefixSum class
prefix_sum_instance = PrefixSum()
# Call the method to calculate prefix sum
prefix_sum_instance.calculate_prefix_sum()
