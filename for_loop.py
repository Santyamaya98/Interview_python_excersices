# Given a number N create its multiplication table with N = (1<=N<=10^8)
# source problem https://www.geeksforgeeks.org/problems/for-loop-python/1&selectedLang=python3

def multiplication_table(N):
    if N == 0:
        print('el resultado es 0')
        return 0 
    N = int(N)
    if isinstance(N, str):
        return('digite un numero (int)')
    table = [num*N for num in range(1,11)]
    print('as string row')
    for i in table:
        print(' '.join(str(i)))
    print('as list')
    return table

if __name__ == "__main__":
    N=input('Enter a number between 0 and 10^8: ')
    print(multiplication_table(N))
