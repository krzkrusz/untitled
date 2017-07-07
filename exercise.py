from random import randint

first_txt = "first"
second_txt = "second"
str_x="X"

with open(first_txt,'w') as firstFile,open(second_txt,'w'):
    for x in range(10):
        firstFile.write(str(randint(1,10)))
        firstFile.write("\n")


with open(first_txt,'r') as input, open(second_txt,'w') as output:
   for line in input:
       output.write(str_x * int(line)+"\n")

