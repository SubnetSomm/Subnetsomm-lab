"""
function_calculator.py
@author: Franco Pisano
Created April 14, 2026
This program shows you how to set up functions that will add, subtract,
multiply, and divide 2 numbers.
The results will look like this when you finish:
10 + 3 = 13
10 - 3 = 7
10 * 3 = 30
10 / 3 = 3.333
"""


def main():
    num1 = 10
    num2 = 3
    add_result = add_numbers(num1, num2)
    subtract_result = subtract_numbers(num1, num2)
    multiply_result = multiply_numbers(num1, num2)
    divide_result = divide_numbers(num1, num2)

    display_results(num1, "+", num2, "=", add_result)
    display_results(num1, "-", num2, "=", subtract_result)
    display_results(num1, "*", num2, "=", multiply_result)
    display_results(num1, "/", num2, "=", divide_result)


def add_numbers(mynum1, mynum2):
    my_add_result = 0
    my_add_result = mynum1 + mynum2
    return my_add_result

def subtract_numbers(mynum1, mynum2):
    my_subtract_result = 0
    my_subtract_result = mynum1 - mynum2
    return my_subtract_result

def multiply_numbers(mynum1, mynum2):
    return mynum1 * mynum2 # this is quicker than initializing and calculating

def divide_numbers(mynum1, mynum2):
    my_divide_result = mynum1 / mynum2
    return my_divide_result


def display_results(mynum1, operator, mynum2, equals, my_result):
    if type(my_result) == int:
        print(f'{mynum1} {operator} {mynum2} {equals} {my_result}')
    else:
        print(f'{mynum1} {operator} {mynum2} {equals} {my_result:.3f}')

# call the main() function
if __name__ == '__main__':
    main()
