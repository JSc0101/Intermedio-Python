## Funciones de order superior ##

def sum_add_value(value):
    return value + 1

def sum_two_number(first_value, second_value):
    return sum_add_value(first_value + second_value)

print(sum_two_number(2,5))

numbers = [1,2,3,4,5,6,7,8,9]

def num_par (number):
    return number % 2 == 0

par = list(filter(num_par, numbers))
print(par)

multiply = list(map(lambda x: x * 2, numbers))
print(multiply)
    
