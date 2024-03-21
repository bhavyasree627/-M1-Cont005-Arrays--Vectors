import sys

def main():
    t = int(input())
    for _ in range(t):
        m, k, a1, ak = map(int, input().split())
        taken_1 = max(0, m % k - a1)
        left_1 = max(0, a1 - m % k)
        taken_k = max(0, m // k - ak)
        to_replace = min(taken_k, left_1 // k)
        ans = taken_1 + taken_k - to_replace
        print(ans)

if __name__ == "__main__":
    main()
