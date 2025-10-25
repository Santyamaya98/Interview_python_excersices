# Given a positive integer x, the task is to print the numbers form 1 to x in the order
# 1^2 2^2 3^2 4^2 5^2  ...
# example x = 10 output 1, 4, 9 constrains 2 <= x <= 10^3
# complexity  o(sqrt(n))
# auxiliary space 0(1)

def jumping_while(x:int) -> int:
    try:
        x = int(x) # I made a mistake here I defined it as  x=int() making x == 0 always
    except:
        return 'value must be integer not string'
    if x == 2 or x == 3 or x == 4:
        return 1
    if x >= 1000:
        return 'digit a number less than 1000'
    i = 0
    powers = []
    result = str()
    while (i**2) < 1000:
        i += 1
        power = i**2
        powers.append(power)
        if powers[-1] > x:
           powers.pop(len(powers)-1)
    result =  ' '.join(str(pow) for pow in powers) # in order to remove "[" "]" u need list comprehension
    return result

if __name__ == "__main__":
    x = input('digite un numero menor a 1000 y mayor a 2 ')
    print(jumping_while(x))




