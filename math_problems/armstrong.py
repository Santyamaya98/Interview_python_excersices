def armstrong(n):
    """
    given a 3 digits number n, find the sume of 3 cubes that is equal to n
    example 371 = 3^3 + 7^3 +  1^3 
    """
    try:
        n=int(n)
    except:
        return 'you must type in an integer of 3 digits'
    n = str(n)
    result = 0

    for i in n:
        i = int(i)
        i = i**3
        result += i

    print(result)
    result = str(result)
    return True if result == n else False

if __name__=="__main__":
    n = input('digit a number of 3 digits: ')
    print(armstrong(n))
