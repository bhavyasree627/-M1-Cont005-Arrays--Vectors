t = int(input()) 
for _ in range(t):
    n = int(input())  
    prices = list(map(int, input().split()))  
    annabelle_age = 20  
    target_price = annabelle_age * 100
    seen_prices = set()
    found = False
    for price in prices:
        complement = target_price - price
        if complement in seen_prices:
            found = True
            break
        seen_prices.add(price)
    if found:
        print("Accepted")
    else:
        print("Rejected")
