#R-1.3 (page 51)

def minmax(data):
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