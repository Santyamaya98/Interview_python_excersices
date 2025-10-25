def geometric_progression(a:int, r:int, n:int) -> int:
    """
    a is the  term r is the ratio n is desiredposition output in the gp
    Input: a = 2, r = 2, n = 4
    Output: 16
    Explanation: The GP series is 2, 4, 8, 16, 32,... in which 16 is the 4th 
    """
    try:
        a = int(a)
        r = int(r)
        n = int(n)
        
    except:
        return 'Please just type in integers up to 10^6'
    if a > 10000000:
        return 'Plesse type a number <= 10^6'
    if n > 10000000:
        return 'Plesse type a number <= 10^6'
    def get_ratio(a,r):
        return a*r
    step = 0
    series = []
    while step <= n:
        series.append(a)
        step += 1
        if step > 0:
            a = get_ratio (a,r)
    if len(series) > 4300:
        return series[n-1]
    result = " ".join(str(series))
    print("result = %s" %(result))
    return series[n-1]


if __name__ == "__main__":
    import sys

    sys.set_int_max_str_digits(10000000)
    a,r,n = input('type int term '), input('type ratio '), input('type the nth numb of the series ')
    print(geometric_progression(a,r,n))
