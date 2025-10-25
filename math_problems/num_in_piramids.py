
def num_piramid(n):
    """	For n= 3,
	pattern:  3 3 3 2 2 2 1 1 1
                    3 3 2 2 1 1 
                    3 2 1
       output list = [3,3,3,2,2,2,1,1,1,-1,3,3,2,2,1,1,-1,3,2,1-1]
    """
    if isinstance(n, str):
        try:
            n = int(n)
        except:
            return "digit an integer <= 40"
    if n > 40:
        return 'digit an integer <= 40'
    output = []
    pattern = []
    x = n
    counter = 0
    repeater = 0
    p = n
    while x > 0:
        pattern.append(x)
        output.append(x)
        counter += 1
        if counter == n:
            x -= 1
            counter = 0
            repeater += 1
        if repeater == p:
            repeater = 0
            output.append(-1)
            pattern.append("\n")
            n -= 1
            x = p
        if  n == 0:
            break
    result_pattern = ",".join(str(patr) for patr in pattern)
    result_output = ",".join(str(out) for out in output)
    return print(result_pattern, result_output)

if __name__ == "__main__":
    n = input('digita un  numero entero entre 1 y 40 ') 
    num_piramid(n)
