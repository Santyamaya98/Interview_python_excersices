def binary_to_decimal(n):
    """It transform binarys to decimal numbers"""
    def check_binary(s):
        valids = {"0", "1", "."}
        input_chars=set(s)
        return input_chars.issubset(valids) and s!= ""
    
    if check_binary(n) == False:
        return print('input is not binary')
    
    n_reverse = [bit for bit in n]
    n_reverse.reverse()
    sumatory = int()
    print(n_reverse)
    for bit in range(len(n_reverse)):
        if n_reverse[bit] == ".":
            entire_part = bit
            break
    entires = n_reverse[(entire_part+1):len(n_reverse)]
    decimals = n_reverse[0:bit]
    print(f"entires {entires}" )
    print(f"decimals {decimals}")
    for bit in range(len(entires)):
        sumatory += int(entires[bit]) * (2**bit)

    counter = len(decimals)
    for bit in range(len(decimals)):
        sumatory += int(decimals[bit]) * (2**(counter*-1))
        counter -= 1
    return print(sumatory)

if __name__ == "__main__":
    n = input('type a binary number ->  ')
    binary_to_decimal(n)