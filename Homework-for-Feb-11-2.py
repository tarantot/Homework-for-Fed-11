my_dict = {'a':645, 'b':3987, 'c': 93, 'd':111, 'e':646, 'f': 20}
my_list =[]
my_list = my_dict.values()
my_list = sorted(my_list ,reverse=True)
#print(my_list[:3])

def get_key(my_dict, value):
    for k, v in my_dict.items():
        if v == value:
            return k
print('Ключ элемента словаря с наибольшим значением: ' + get_key(my_dict, my_list[0]))
print('Ключ элемента словаря со вторым наибольшим значением: ' + get_key(my_dict, my_list[1]))
print('Ключ элемента словаря с третьим наибольшим значением: ' + get_key(my_dict, my_list[2]))