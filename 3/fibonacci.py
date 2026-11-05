# Fibonacci using Non-Recursive Method
def fibonacci_iterative(n):
    a, b = 0, 1

    print("Fibonacci Series (Non-Recursive):")

    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b


# Fibonacci using Recursive Method
def fibonacci_recursive(n):
    if n <= 1:
        return n

    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


# Main Program
n = int(input("Enter the number of terms: "))

if n <= 0:
    print("Please enter a positive number.")
else:
    fibonacci_iterative(n)

    print("\nFibonacci Series (Recursive):")
    for i in range(n):
        print(fibonacci_recursive(i), end=" ")


'''
Enter the number of terms: 7

Fibonacci Series (Non-Recursive):
0 1 1 2 3 5 8

Fibonacci Series (Recursive):
0 1 1 2 3 5 8






Fibonacci Series – Theory
The Fibonacci Series is a sequence of numbers in which each number is the sum of the previous two numbers. It starts with 0 and 1.

Example: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34 ...

Formula:
\[
F(n) = F(n-1) + F(n-2)
\]

Base conditions:
- F(0) = 0
- F(1) = 1

Methods Used
1. Non-Recursive Method (Iterative):
- Uses a for loop to generate Fibonacci numbers.
- Stores the previous two numbers in variables.
- Adds them to calculate the next number.
- Updates the variables in each iteration.

2. Recursive Method:
- Uses a function that calls itself.
- Calculates the sum of the previous two Fibonacci numbers.
- Uses base conditions to stop recursive calls.

Time and Space Complexity

Method	   Time Complexity	Space Complexity
Non-Recursive	O(n)  |          O(1)
Recursive	    O(2ⁿ) |          O(n)
'''