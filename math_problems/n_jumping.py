def find_jump_n(n):
    """It finds the largest jumping x equal or smaller than n """
    try:
        int(n)
    except:
        return print(f'{n} is not an int')
    
    if int(n)  <= 10:
        return n
    pointerone = 1 
    while int(n) >= 10:
        if int(n) == 10:
            return n
        for num in n:
            if pointerone > len(n)-1:
                return n 
            pointer = int(num)
            x = pointer - int(n[pointerone])
            if x == 1 or x == -1:
                pointerone += 1  
            elif x > 1 or x < -1:
                n = int(n) - 1
                n = str(n)   
                pointerone = 1   
                break   
            else:
                n = int(n) - 1
                n = str(n)
                pointerone = 1 
                break
            
    return n


if __name__ == "__main__":
    n = input('type an integer --->  ')
    print(find_jump_n(n))