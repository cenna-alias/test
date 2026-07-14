arr = [6,7,2,8,3]
Sum = 0
Min = arr[0]
Max = arr[0]

for num in arr:
    Sum += num

for i in range(1, len(arr)):
    if arr[i] < Min:
        Min = arr[i]

for i in range(1, len(arr)):
    if arr[i] > Max:
        Max = arr[i]

print("Sum of all elements in the array:", Sum)
print("Minimum element in the array:", Min)
print("Maximum element in the array:", Max)
