n = int(input())

# list of denominations 
denominations = [100, 50, 20, 10, 5, 2, 1]

print(n)

for denom in denominations:
    count = n // denom      # Calculate the number of notes of this denomination
    n = n % denom           # Update the remaining amount
    print(f"{count} nota(s) de R$ {denom},00")


