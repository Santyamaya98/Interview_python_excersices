# given a number n 
# n can be negative or positive
# if n is negative print n to 0 adding 1
# if n is positive print n to 0  subtracting 1 
# in = 4 output = 3 2 1 0

def zero_convert(x:int) -> 0:
    if isinstance(x,str):
        try:
            x = int(x)
        except:
            return 'input must be an integer negative or positive'
    numbs = []
    i = x
    while i < 0 or i > 0:
        if i == 0:
            break
        if i > 0:
            i -= 1
            numbs.append(i)
        if i < 0:
            i += 1
            numbs.append(i)

    result =  " ".join(str(num) for num in numbs)
    return result
if __name__ == "__main__":
    x = input('digit a positive or negative number ')
    print(zero_convert(x))
