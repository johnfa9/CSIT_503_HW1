#R – 1.11 (page 51)

def exp(n):
    """Demonstrate how to use Python’s list comprehension syntax to produce the list [1, 2, 4, 8, 16, 32, 64, 128, 256]"""
    return [2 ** k for k in range(0, n)]
print(exp(9))