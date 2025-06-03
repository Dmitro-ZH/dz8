while True:
    n = input()
    amount = int(n[0:n.find(" ")])
    if amount < 10 or amount > 999:
        break
    n = n[(n.find(" ")+1):]
    colors = {
        1:0,
        2:0,
        3:0,
        4:0,
        5:0,
        6:0,
        7:0,
        8:0
    }

    for i in n:
        if i == " ":
            continue
        else:
            colors[int(i)] += 1

    print(f"1 {colors[1]} 2 {colors[2]} 3 {colors[3]} 4 {colors[4]} 5 {colors[5]} 6 {colors[6]} 7 {colors[7]} 8 {colors[8]}")

    break