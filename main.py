cat = True
k = input()
amount = int(k[0:k.find(" ")])
weights = k[(k.find(" ")+1):]
while cat:
    if amount > 100 or amount < 1:
        break
    else:
        fish_weight = []
        for i in range(amount):
            if i != (amount-1) :
                fish = weights[0:weights.find(" ")]
                fish_weight.append(int(fish))
                weights = weights[(weights.find(" ")+1):]
            else:
                fish_weight.append(int(weights))

        fish_weight.sort()
        weight = 0
        for i in fish_weight:
            if i > 1000:
                break
            else:
                weight += i

        print(f"{fish_weight[0]} {fish_weight[-1]} {weight}")
    break