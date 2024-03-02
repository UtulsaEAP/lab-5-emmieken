
'''''''''
Name: Emmie Kennemer
Date: 2/29/24
'''''''''

def fibonacci(n):
    if n == 0:
        return(0)
    if n == 1:
        return(1)
    nth_term = fibonacci(n-1) + fibonacci(n-2)
    return(nth_term)

    
if __name__ == '__main__':
    start_num = int(input())

    print(f'fibonacci({start_num}) is {fibonacci(start_num)}')