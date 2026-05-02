my_budget = 450000

shop_quotes = [48000, 445000, 460000, 420000, 500000]

for price in shop_quotes: 
    if price <= my_budget:
        change = my_budget - price
        print(f"Deal found: {price} PKR. You have {change} PKR left over.")
    else:
        print(f"Quote rejected: {price} PKR. Too expensive.")
