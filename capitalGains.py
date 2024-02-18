class Capital:

    totalGain = 0
    totalYears = int(input("Over how many years did the customer purchase Stock X: "))
    for x in range(totalYears):
        unitsAmount = int(input("How many units did the customer purchase in the year: "))
        price = int(input("At what price per share?: "))
        totalGain += (unitsAmount*price)
        print(totalGain)
    sell = int(input("How many units did the customer sell?: "))
    price2 = int(input("At what price per share?: "))
    totalGain -= (sell*price2)
    print(totalGain)
