def find_greatest(a,b,c):
    # to find the greatest between a and b 
    greatest_ab = (a + b + abs(a - b)) // 2
    greatest = (greatest_ab + c + abs(greatest_ab - c)) // 2 
    return greatest

a, b, c = map(int, input().split())

greatest_number = find_greatest(a, b, c)

print(f"{greatest_number} eh o maior")
    