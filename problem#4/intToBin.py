'''
Name: Emmie Kennemer
Date: 2/29/24
'''

def int_to_reverse_binary(user_num):
    binary_val = ''
    while user_num > 0:
        binary_val += str(user_num % 2) 
        user_num = user_num//2 
    return binary_val


def string_reverse(input_string): 
    return input_string [::-1]
    
    #for i in int_to_reverse_binary(user_num):
     #   input_string = i + reverse_input
    #return input_string 


if __name__ == '__main__':
    user_num = int(input())
    binary_string = int_to_reverse_binary(user_num)
    print(string_reverse(binary_string))


