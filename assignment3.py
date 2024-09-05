def calculate_discount(price,discount_percent):
 if discount_percent>=20:
    discount=discount_percent*price
    return discount
 else:
   return price
price=int(input("Enter original price:"))

discount_percent=float(input("Enter discount percentage:"))
print("Final price:",calculate_discount(price,discount_percent))