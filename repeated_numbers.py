#hi
t = int(input())
for i in range(t):
    a = int(input())
    l = list(map(int, input().split()))
    d = set()
    s = []
    for j in range(len(l)): 
            if l[j] not in d:
                d.add(l[j])
            else:
                s.append(l[j])
    s.sort()
    for k in s:
        print(k, end=" ")
    print()