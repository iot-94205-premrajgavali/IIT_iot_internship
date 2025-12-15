num1 = int(input("Enter a 5 digit number: "))

right = num1
rev = 0

while num1 > 0:
    dig = num1 % 10
    rev = rev * 10 + dig
    num1 = num1 // 10   

if right == rev:
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")
