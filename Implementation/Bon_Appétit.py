list_length,index = input().split()
xs = list(map(int,input().strip().split(" ")))
bill = input()
bill = float(bill)
allergy = xs.pop(int(index))
price = 0
for i in range(len(xs)):
    price += xs[i]
price = price / 2
if price == bill:
    print("Bon Appetit")
else:
    print(int(bill-price))
