def mergeSort(arr):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2

    left, left_inversions = mergeSort(arr[:mid])
    right, right_inversions = mergeSort(arr[mid:])

    merged, merge_inversions = merge(left, right)

    total_inversions = left_inversions + right_inversions + merge_inversions

    return merged, total_inversions

def merge(left, right):
    merged = []
    inversions = 0
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
            inversions += len(left) - i

    while i < len(left):
        merged.append(left[i])
        i += 1

    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged, inversions

t = int(input())

input()

for _ in range(t):
    n = int(input())
    arr = [int(input()) for _ in range(n)]
    input()

    _, inversions = mergeSort(arr)
    print(inversions)