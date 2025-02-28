import re

lst = ["Краснодарский - завод", "Директор: Карпенко"]

for i in lst:
    i = i.replace(" ", "")
    new_lst = re.split(":|-", i)
    print(new_lst)
