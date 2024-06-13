# seller name 
# seller salary 
# seller gets 15% commission over the whole sale he has made 

name = input()
salary = float(input())
total_sale = float(input())

total = .15 * total_sale + salary
print('TOTAL = R$ {:.2f}'.format(total))