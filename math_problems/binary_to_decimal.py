def binary_to_decimal(n):
    """It transform binarys to decimal numbers"""
    def check_binary(s):
        valids = {"0", "1"}
        input_chars=set(s)
        return input_chars.issubset(valids) and s!= ""
    
    if check_binary(n) == False:
        return print('input is not binary')
    
    n_reverse = [bit for bit in n]
    n_reverse.reverse()
    sumatory = int()
    print(n_reverse)
    for bit in range(len(n_reverse)):
        sumatory += int(n_reverse[bit]) * (2**bit)
    
    return print(sumatory)

if __name__ == "__main__":
    n = input('type a binary number ->  ')
    binary_to_decimal(n)