# hours:minutes:seconds

n = int(input())

hour = n // 3600 
n = n % 3600
min = n // 60 
sec = n % 60 

print(f"{hour}:{min}:{sec}") 
