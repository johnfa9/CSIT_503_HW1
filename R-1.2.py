#R-1.2 (page 51)
def is_Even(val) :
    """Write a short Python function, is_even(k), that takes an integer value and returns True if k is even,
    and False otherwise. However, your function cannot use the multiplication, modulo, or division operators."""
    return (val & 1);

val = int(input("Enter a number: "))
if(is_Even(val) == 0):
    print ("The number", val, "is even")
else :
    print("The number", val, "is odd")
