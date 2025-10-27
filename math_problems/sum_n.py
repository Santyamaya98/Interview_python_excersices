def sum_digit_n(n):
    """
    sum each digit of  number n 
    """
    try:
        n = int(n)
    except:
        return "type an integer"
    if n > 1000000:
        return
    n = str(n)
    result = 0
    for i in n:
        i = int(i)
        result += i
    return result
if __name__=="__main__":
    n = input('digit a number ')
    print(sum_digit_n(n))
