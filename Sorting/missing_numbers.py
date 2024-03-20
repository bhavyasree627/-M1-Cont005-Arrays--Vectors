def missingNumbers(arr, brr):
    arr_freq = {}
    brr_freq = {}
    for num in arr:
        if num in arr_freq:
            arr_freq[num] += 1
        else:
            arr_freq[num] = 1
    for num in brr:
        if num in brr_freq:
            brr_freq[num] += 1
        else:
            brr_freq[num] = 1
    missing_numbers = set()
    for num, count in brr_freq.items():
        if num not in arr_freq or arr_freq[num] < count:
            missing_numbers.add(num)
    return sorted(missing_numbers)

n1=int(input())
arr = list(map(int,input().split()))
n2=int(input())
brr=list(map(int,input().split()))
print(*missingNumbers(arr, brr)) 