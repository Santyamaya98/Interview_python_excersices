
def max_abs_val(n,m):
    """
    Given two integers n and m (m != 0). The problem is to find 
    the number closest to n and divisible by m. If there is more
    than one such number, then output the one having the maximum
    absolute value.
    Input: n = -15, m = 6
    Output: -18
    Explanation: Both -12 and -18 are closest to -15 and divisible by 6, 
    but -18 has the maximum absolute value. So, output is -18. 
    """
    try:
        n = int(n)
        m = int(m)
    except:
        return 'type an integer between -10^5 and 10^5'
    if n == 0 or m == 0:
        return 'n and m must be != 0'
    if n % m == 0:
        return n
    case_a = []
    true_n = n
    pos = n
    neg = n
    case_b = []
    output_a, output_b = int(), int()
    while True:
        pos += 1
        neg -= 1 
        if pos % m == 0:
            case_a.append(pos)
        if neg % m == 0:
            case_b.append(neg)
        if len(case_a) > 0 and len(case_b) > 0:
            if abs(case_a[-1]) < abs(case_b[-1]):
                output_a = abs(case_a[-1])
            else: 
                output_b = abs(case_b[-1])
            if (output_a - n) < (output_b - n) and len(case_a) > n or len(case_b) > n:
                return output_a
            else:
                return output_b
        n -= 1 
        if n <= 0:
            break
    return min(output_a, output_b), print(case_a,case_b)

if __name__ == "__main__":
    n,m = input('n = '), input('m = ')
    print(max_abs_val(n,m))
