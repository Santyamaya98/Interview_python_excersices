#https://www.geeksforgeeks.org/problems/for-loop-2-python/1&selectedLang=python3
def print_even_in_string_cell(strings:str) -> str:
    """It will return just even cells of provided string chain"""
    evens = []
    for i in range(0, len(strings), 2): 
        evens.append(strings[i])
        result= "".join(evens)
    return result

if __name__=="__main__":
    strings = input("Write a String: ")
    print(print_even_in_string_cell(strings))
