def add(a , b):
    return a+b 

def multiply(a , b ):
    return a * b

def divide(a, b):
    return a/b

def calculator(operation , a , b):
    return operation(a, b)


print(calculator(add , 1, 2))

def calLambda(operation , n1 , n2 ):
    return operation(n1 , n2)

# For the calculator method, we needed to write 3 extra functions that could be used as the argument. This can be quite a hassle.
#Why don’t we just pass a lambda as the argument? The 3 operations are pretty simple, so they can be written as lambdas.

print(calLambda(lambda n1 , n2 : n1 * n2 , 10 , 20))


# Built in map function
num_list = [0 ,1, 2, 3, 4, 5]
double_list = map(lambda n : n *2 , num_list);

print(double_list)

print(list(double_list));

# Filter and Sum

input = [30, 2, -15, 17, 9, 100]

filtered_list = list(filter(lambda a : a> 10 , input ))

print(filtered_list)