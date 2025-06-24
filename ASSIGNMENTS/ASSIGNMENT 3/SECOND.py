n = int(input("Enter a number: "))
def palindrome(n):
     return str(n) == str(n)[::-1]
if palindrome(n):
        print("The number is a palindrome")
else:
        print("The number is not a palindrome")