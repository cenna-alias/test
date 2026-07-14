str = "malayalam"
is_palindrome = True
left = 0
right = len(str) - 1
while left < right:
    if str[left] != str[right]:
        is_palindrome = False
        break
    left += 1
    right -= 1
if is_palindrome:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
