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

class Solution:
    def jumpingNums(n):
        n = int(n)
        if n <= 10:
            return n
        
        max_jump = 0
        queue = list(range(1, 10))  # Start from digits 1-9
        
        while queue:
            num = queue.pop(0)
            if num > n:
                continue
            max_jump = max(max_jump, num)
            #print(f'max_jump: {max_jump}')
            last_digit = num % 10
            #print(f'last_digit: {last_digit}')
            # Append next possible digits
            for next_digit in [last_digit - 1, last_digit + 1]:
                #print(f'next_digit: {next_digit}')
                if 0 <= next_digit <= 9:
                    new_num = num * 10 + next_digit
                    if new_num <= n:
                        queue.append(new_num)
        
        return print(max_jump)   


if __name__ == "__main__":
    n = input('type an integer --->  ')
    print(find_jump_n(n))
    obj = Solution.jumpingNums(n)
    obj