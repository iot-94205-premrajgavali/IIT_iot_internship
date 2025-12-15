def fibonacci(num1):
    a, b = 0, 1
    for i in range(num1):
        print(a, end=" ")
        a, b = b, a + b

# take input from user
n = int(input("Enter number of terms: "))

# call the function
fibonacci(n)
