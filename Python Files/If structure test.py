order_total = 50
quantity = 10

if quantity == 1 or quantity == 2:
    discount = 0
elif quantity >= 3 and quantity < 10:
    discount = order_total * .1
elif quantity > 10 and quantity <= 25:
    discount = order_total * .2
else:
    discount = order_total * .3

print(discount)