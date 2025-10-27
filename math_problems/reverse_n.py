def reverse_n(n):
    """
    Given the number n it returns the reverse without zeros
    """
    try:
        n = int(n)
    except:
        return 'type in an integer'
    n = str(n)
    reverse_list = []
    for i in n:
        if i == '0':
            pass
        else:
            reverse_list.append(i)
    reverse_list.reverse()
    return "".join(reverse_list)

if __name__=="__main__":
    n = input('type in a number n ')
    print(reverse_n(n))
