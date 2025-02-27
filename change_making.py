def make_change(target_amount):
    denominations = [200,100,50,20,10,5,2,1]
    coins_count = 0
    values = []
    for coin in denominations:
        while target_amount >= coin:
            target_amount -= coin
            values.append(coin)
            coins_count += 1
    return coins_count ,values


print(make_change(24))
print(make_change(163))