t = int(input())
for i in range(t):
    l = list(map(int, input().split()))
    count=0
    for j in range(l[0], l[1]+1):
        if(j%10==2 or j%10==3 or j%10==9):
            count += 1
    print(count)