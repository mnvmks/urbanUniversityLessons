# module_2_3 - while loop

my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

while len(my_list) > 0:
    if my_list[0] < 0:
        break
    elif my_list[0] == 0:
        my_list.pop(0)
        continue
    elif my_list[0] > 0:
        print(my_list.pop(0))
