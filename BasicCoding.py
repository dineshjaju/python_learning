def rep_cat(x, y):
    result = ''
    for i in range(x):
        result += str(x)
    for j in range(y):
        result += str(y)
    return result

print(rep_cat(3, 4).__str__())  # Corrected to call __str__() method directly on the result
