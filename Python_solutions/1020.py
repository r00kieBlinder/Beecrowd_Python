# Age in Days 
# years, months, days 

n = int(input())

years = n // 365 
n = n % 365 
months = n // 30 
days = n % 30

print(f"{years} ano(s)")
print(f"{months} mes(es)")
print(f"{days} dia(s)")
