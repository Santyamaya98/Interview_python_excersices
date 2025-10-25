def num_series(a1, a2, n):
    """
     calculate the n-th num of the serie a1, a2
     Input: a1 = 1, a2 = 3, n = 10
     Output: 19
     Explanation: The series is: 1,3,5,7,9,11,13,15,17,19,21.. Thus, the 10th term is 19.
    """
    try:
        a1 = int(a1)
        a2 = int(a2)
        n = int(n)
    except:
        return 'a1: debe ser un int < a2, a2: debe ser un int mayor a a1, n es la posicion de la secuencia de tipo int'
    def calcul_step(a1,a2):
        return a2-a1
    step = 0
    secuence = []
    while step <= n:
        if step == 0:
            secuence.append(a1)
            secuence.append(a2)
            step += 2
        if step >= 2:
            a2 = a2 + calcul_step(a1,a2)
            a1 = secuence[-1]
            secuence.append(a2)
            step += 1
    result =  " ".join(str(sec) for sec in secuence)
    print('secuence: %s ' %(result))
    return 'output = %s ' %(secuence[n-1])
if __name__ == "__main__":
    a1, a2, n = input('digit first secuence num '), input('input the second num of the secuence '), input('the n-th number you want ')
    print(num_series(a1,a2,n))
