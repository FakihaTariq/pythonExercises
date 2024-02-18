good_credit = True
house_price = 1000000.0
down_payment = 0

if good_credit:
    down_payment = house_price * .10
else:
    down_payment = house_price * .20
print(f'Down Payment: ${down_payment}')

