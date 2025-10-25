# Given a number N create its multiplication table with N = (1<=N<=10^8)
# source problem https://www.geeksforgeeks.org/problems/for-loop-python/1&selectedLang=python3

def multiplication_table(N):
    if N == 0:return 0
    if N is str:return ('digite un numero')
    N = int(N)
    result = [n for n in range(1,10)]
    return result

if __name__ == "__main__":
    N=input('Enter a number between 0 and 10^8')
    multiplication_table(N)
