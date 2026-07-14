arr = [4, 3, 6, 9, 8]
print("Reversed array without changing values :")
for i in range(len(arr)-1, -1, -1):
    print(arr[i], end=' ')
print()

left = 0
right = len(arr) - 1
while left < right:
    arr[left], arr[right] = arr[right], arr[left]
    left += 1
    right -= 1
print("Reversed array:", arr)