import os

my_str = "Hello Academy"
str2 = "Hi"

age = 24
name = "Krzysztof"
output=my_str + str2 + "  " +str2

str_template = "my name is {}.I am {} years old."

print(str_template.format(name,age))

def add_vegetable(vegetable='carrot', list_of_vegetables=[]):
    list_of_vegetables.append(vegetable)
    return list_of_vegetables

first_list = add_vegetable()
second_list = add_vegetable('banana')

print(first_list)
print(second_list)
