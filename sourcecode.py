lst = list(map(int, input("Enter the values ").split()))
count = 0
for numbers in lst:
    count += 1
max = lst[0]
for i in lst:
    if i > max:
        max = i
print(max)        
    
