## Lambdas ##

result = lambda first__value,second__values: first__value + second__values

print(result(2,2))

my__List = [10,20,30,40,50,77]
list__result = filter(lambda x: x % 2 == 0, my__List)

print(list(list__result))

result__ = list(map(lambda sum: sum, my__List))

for values in result__:
    print(values)

multiply = lambda num__one, num__two: num__one * num__two 

print(multiply(20,20))