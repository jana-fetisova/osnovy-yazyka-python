from random import randint

my_list = [randint(-10, 10) for _ in range(20)]

check = set()
uniq = set()
for el in my_list:
    if el not in check:
        check.add(el)
        uniq.add(el)
    else:
        if el in uniq:
            uniq.remove(el)

print(uniq)