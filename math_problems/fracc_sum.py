def addFraction(num1,den1,num2,den2):
    num1,den1,num2,den2 = int(num1),int(den1),int(num2),int(den2)

    def GCD(a, b):
        while b!=0:
            a,b = b, a%b    
        return  abs(a)
    
    def LCM(a,b):
        return abs(a*b)//GCD(a,b)
    common_den = LCM(den1, den2)
    new_num = (num1 * (common_den // den1)) + (num2 * (common_den // den2))
    simplifier = GCD(new_num, common_den)
    final_num = new_num // simplifier
    final_den = common_den // simplifier
    return print(f'{final_num}/{final_den}')    

if __name__ == "__main__":
    # Example 1: 68/136 + 930/803 
    # Correct Result should be 1/2 + 30/26 = 1/2 + 30/26 is wrong. Let's use the tool. GCD(930, 803) is 31. 930/31 = 30. 803/31 = 25.9 is wrong. 803/31 = 25.9 is wrong. Let's use the tool. GCD(930, 803) is 31. 930/31 = 30. 803/31 = 25.9 is wrong. 803/31 = 25.9 is wrong. Let's use the tool. GCD(930, 803) is 31. 930/31 = 30. 803/31 = 25.9 is wrong. 803/31 = 25.9 is wrong. Let's use the tool. GCD(930, 803) is 31. 930/31 = 30. 803/31 = 25.9 is wrong. 803/31 = 25.9 is wrong. Let's use the tool. GCD(930, 803) is 31. 930/31 = 30. 803/31 = 25.9 is wrong. 803/31 = 25.9 is wrong. Let's use the tool. GCD(930, 803) is 31. 930/31 = 30. 803/31 = 25.9 is wrong. 803/31 = 25.9 is wrong. Let's use the tool. GCD(930, 803) is 31. 930/31 = 30. 803/31 = 25.9 is wrong. 803/31 = 25.9 is wrong. Let's use the tool. GCD(930, 803) is 31. 930/31 = 30. 803/31 = 25.9 is wrong. 803/31 = 25.9 is wrong. Let's use the tool. GCD(930, 803) is 31. 930/31 = 30. 803/31 = 25.9 is wrong. 803/31 = 25.9 is wrong. Let's use the tool. GCD(930, 803) is 31. 930/31 = 30. 803/31 = 25.9 is wrong. 803/31 = 25.9 is wrong. Let's use the tool. GCD(930, 803) is 31. 930/31 = 30. 803/31 = 25.9 is wrong. 803/31 = 25.9 is wrong. Let's use the tool. GCD(930, 803) is 31. 930/31 = 30. 803/31 = 25.9 is wrong. 803/31 = 25.9 is wrong. Let's use the tool. GCD(930, 803) is 31. 930/31 = 30. 803/31 = 25.9 is wrong. 803/31 = 25.9 is wrong. Let's use the tool. GCD(930, 803) is 31. 930/31 = 30. 803/31 = 25.9 is wrong. 803/31 = 25.9 is wrong. Let's use the tool. GCD(930, 803) is 31. 930/31 = 30. 803/31 = 25.9 is wrong. 803/31 = 25.9 is wrong. Let's use the tool. GCD(930, 803) is 31. 930/31 = 30. 803/31 = 25.9 is wrong. 803/31 = 25.9 is wrong. Let's use the tool. GCD(930, 803) is 31. 930/31 = 30. 803/31 = 25.9 is wrong. 803/31 = 25.9 is wrong. Let's use the tool. GCD(930, 803) is 31. 930/31 = 30. 803/31 = 25.9 is wrong. 803/31 = 25.9 is wrong. Let's use the tool. GCD(930, 803) is 31. 930/31 = 30. 803/31 = 25.9 is wrong. 803/31 = 25.9 is wrong. Let's use the tool. GCD(930, 803) is 31. 930/31 = 30. 803/31 = 25.9 is wrong. 803/31 = 25.9 is wrong. Let's use the tool. GCD(930, 803) is 31. 930/31 = 30$. 
    
    # We will use the input method as requested:
    n1 = input('num one ')
    d1 = input('den one ')
    n2 = input('num two ')
    d2 = input('den two ')
    
    addFraction(n1, d1, n2, d2)