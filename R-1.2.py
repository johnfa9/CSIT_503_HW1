#R-1.2 (page 51)
def is_Even(val) :
    return (val & 1);

val = int(input("Enter a number: "))
if(is_Even(val) == 0):
    print ("The number", val, "is even")
else :
    print("The number", val, "is odd")
