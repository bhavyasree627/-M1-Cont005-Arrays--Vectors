import heapq
def custom_sort(N, M, nums):
    count_dict = {}
    for num in nums:
        count_dict[num] = count_dict.get(num, 0) + 1
    min_heap = []
    for num, count in count_dict.items():
        heapq.heappush(min_heap, (-count, num))
    result = []
    while min_heap:
        count, num = heapq.heappop(min_heap)
        count = -count
        result.extend([num] * count)
    return result

N, M = map(int, input().split())
nums = list(map(int, input().split()))
output = custom_sort(N, M, nums)
print(*output)
