n = int(input("Enter a number: "))
esum = 0
osum = 0
for i in range(1, n+1, 2):
    osum += i
for i in range(2, n+1, 2):
    esum += i
print("Sum of odd numbers from 1 to", n, ":", osum)
print("Sum of even numbers from 1 to", n, ":", esum)