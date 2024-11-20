immutable_var = 1, 2, 3, 'apple', True, 0
print(immutable_var)
# immutable_var[0][0] = 2  # Не поддерживает обращение по элементам и выдает ошибку
mutable_list = ([1, 2, 3, 'apple', True], 0)
print(mutable_list)
mutable_list[0][0]=2
print(mutable_list)
mutable_list[0][3]='table'
mutable_list[0][4]=False
print(mutable_list)