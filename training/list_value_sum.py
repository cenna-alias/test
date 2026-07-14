arr = [8,7,3,4,5]

oisum = 0
eisum = 0
ovsum = 0
evsum = 0

for i in range(0, len(arr), 2):
        eisum += arr[i]
for i in range(1, len(arr), 2):
        oisum += arr[i]
for num in arr:
    if num%2 == 0:
        evsum += num
    else:
        ovsum += num

print("Sum of elements at odd indices:", oisum)
print("Sum of elements at even indices:", eisum)
print("Sum of odd elements in the array:", ovsum)
print("Sum of even elements in the array:", evsum)