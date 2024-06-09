def my_function(n):
    # Your code here
    max_value = n[0]
    for i in n:
        if i > max_value:
            max_value = i
    return max_value


my_list = [1001, 9, 100, 0]
assert my_function(my_list) == 1001

my_list = [1, 9, 9, 0]
print(my_function(my_list))
