a = int(input())
for cc in range(a):
    aa = list(map(int, input().split(" ")))
    b = list(map(int, input().split(" ")))
    c = list(map(int, input().split(" ")))
    bm = []
    sm = []
    mm = b[0]
    bm.append(mm)
    sm.append(mm)
    for x in range(1, len(b)):
        mm = max(b[x], mm)
        bm.append(mm)
        sm.append(sm[-1] + b[x])
    ans = []
    for k in range(len(c)):
        le = c[k]
        mini = 0
        maxi = len(b) - 1
        la = -1
        while mini <= maxi:
            mid = (mini + maxi) // 2
            if le >= bm[mid]:
                la = mid
                mini = mid + 1
            else:
                maxi = mid - 1
        if la == -1:
            ans.append("0")
        else:
            ans.append(str(sm[la]))
    print(" ".join(ans))
