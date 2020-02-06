#R-1.3 (page 51)

def minmax(data):
    """Write a short Python function, minmax(data), that takes a sequence of one or more numbers, and returns the
     smallest and largest numbers, in the form of a tuple of length two. Do not use the built-in functions min or max
     in implementing your solution."""
    min = data[0]
    max = data[0]
    for i in data:
        if i < min:
            min = i
        if i > max:
            max = i
    f = min,max
    return f
print(minmax([7, 1, 20, 3, -3, 900,5]))