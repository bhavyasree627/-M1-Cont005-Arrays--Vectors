import sys

def upperBound(a, k):
    lo, hi = -1, len(a)
    while hi - lo > 1:
        mid = lo + (hi - lo) // 2
        if a[mid][0] > k:
            hi = mid
        else:
            lo = mid
    return hi
def work():
    s, b = map(int, input().split())
    a = list(map(int, input().split()))
    bases = [tuple(map(int, input().split())) for _ in range(b)]
    bases.sort()
    for i in range(1, b):
        bases[i] = (bases[i][0], bases[i][1] + bases[i - 1][1])
    for i in a:
        it = upperBound(bases, i)
        print(0 if it == 0 else bases[it - 1][1], end=" ")
    print()
def main():
    t = 1
    # t = int(input())
    for _ in range(t):
        work()
if __name__ == "__main__":
    main()
