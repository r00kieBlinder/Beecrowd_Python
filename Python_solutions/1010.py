a = input().split()
code_a, numberOfProducts_a, price_perUnit_a = a 

b = input().split()
code_b, numberOfProducts_b, price_perUnit_b = b

total = float(int(numberOfProducts_a) * float(price_perUnit_a) + int(numberOfProducts_b) * float(price_perUnit_b))
print('VALOR A PAGAR: R$ {:.2f}'.format(total))
