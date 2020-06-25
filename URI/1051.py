money = float(input())

if 0.00<=money<=2000.00:
	print("Isento")

elif 2000.01<=money<=3000.00:
	pay = money-2000.00
	finalPay = pay*0.08
	print("R$ %.2f" % (finalPay))

elif 3000.01<=money<=4500.00:
	base = 80.00
	pay = money-3000.00
	pay2 = pay*0.18
	finalPay = base+pay2
	print("R$ %.2f" % (finalPay))

elif money>4500.00:
	base = 80.00+270.00
	pay = money-4500.00
	pay2 = pay*0.28
	finalPay = base+pay2
	print("R$ %.2f" % (finalPay))