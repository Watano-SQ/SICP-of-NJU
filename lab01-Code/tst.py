def factorial(n):
    """Return the factorial of a non-negative integer n.

    >>> factorial(3)
    6
    >>> factorial(5)
    120
    """
    "*** YOUR CODE HERE ***"
    if n == 0:
        return 1
    elif n > 0 :
        i = 1
        fact = 1
        while i <= n:
            fact *= i
            i += 1
        return fact
    
print(factorial(3),factorial(5))
