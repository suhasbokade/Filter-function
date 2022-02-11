input_list = [1, "3","5", "hello", 7, 2.0]
no_list = list(filter(lambda x: isinstance(x, int), input_list))
print(no_list)
