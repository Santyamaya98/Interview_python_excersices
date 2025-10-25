# https://www.geeksforgeeks.org/problems/while-loop-in-python/1&selectedLang=python3
def return_nums_to_cero(N:int) -> str:
    """Given a number x, the task is to print the numbers 
    from x to 0 in decreasing order in a single line"""
    N = int(N)
    display = []
    if isinstance(N, str):
        return 'enter a num base 10 int type'
    while N > 0:
        if N == 0:
            display.append(N)
            break
        display.append(N)
        N-=1
    return "".join(str(display))

if __name__ == "__main__":
    N = input('type an int: ')
    print(return_nums_to_cero(N))
