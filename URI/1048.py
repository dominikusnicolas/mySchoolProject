salary = float(input())

if 0<= salary <= 400.00:
	percentage = 0.15
elif 400.01<= salary <= 800.00:
	percentage = 0.12
elif 800.01<= salary <= 1200.00:
	percentage = 0.1
elif 1200.01<= salary <= 2000.00:
	percentage = 0.07
elif salary > 2000.00:
	percentage = 0.04

money = percentage*salary
newSalary = salary+ money
percentageOutput = int(percentage*100)

print("Novo salario: %.2f" % (newSalary))
print("Reajuste ganho: %.2f" % (money))
print("Em percentual: %i %%" % (percentageOutput))