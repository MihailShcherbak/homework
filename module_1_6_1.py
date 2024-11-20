my_dict = {'Ivan':2002,'Mikhail':1980,'Alla':1982,'Anastasiya':2006}
print('Словарь:',my_dict)
print('Существующее значение:',my_dict.get('Mikhail'))
print('Не существующее значение:',my_dict.get('Mariya'))
my_dict.update({'Mariya':1985,'Andrey':1995})
print('Удалённое значение',my_dict.pop('Alla'))
print('Измененный словарь:',my_dict)
my_set = {1,2,3,4,5,'Alla',1,2,3,4,5,'Alla','Alla',True,True,False}
print('Множество:',my_set) # Почему-то не отобразилось значение True? У вас в уроке тоже... Почему?
my_set.add(7)
my_set.add('Егор')
my_set.remove(1)
print('Изменённое множество:',my_set)