def outer_funtion(x):
    def inner_funtion(y):
        return y * 2
    return inner_funtion(x)

result = outer_funtion(5)

print(result)