n = int(input("Enter a number: "))
sum = 0
temp = n
count = 0 

while temp > 0:
    count += 1
    temp //= 10

temp = n

while temp > 0:
    rem = temp % 10
    sum += rem ** count
    temp //= 10

if sum == n:
    print(n, "is an Armstrong number")
else:
    print(n, "is not an Armstrong number")
