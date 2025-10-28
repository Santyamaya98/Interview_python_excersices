def kth_num(a,b,k):
    """
    it must return the k values of the output number of a^b from right to left
    """
    k = int(k)
    c = int(a)**int(b)
    c = str(c)
    if k == 0:
        k = -1
        return c[k]
    try:
        result = c[-k]
    except IndexError:
        print('%s is out of range ' %k)
        return 'for this case k must be between 1 and ', len(c)
    return c[-k]


def kth_math(a,b,k):
    a,b,k = int(a),int(b),int(k)
    r = a**b
    mod = 10**k
    div = 10**(k-1)
    R = pow(a,b,mod)
    return  R//div % 10
if __name__=="__main__":
    a,b,k=input('digit a: '),input('b: '), input('k: ')
    print(kth_num(a,b,k))
    print(kth_math(a,b,k))
