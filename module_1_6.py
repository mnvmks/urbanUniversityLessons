# module_1_6.py

# dict type
my_dict = {"Ivan": 1994, "Petr": 1990, "Serj": 1986}
print("Dict:", my_dict, sep=" ")
print("Existing value: ", my_dict["Ivan"],
      "\nNot existing value: ", my_dict.get("Olga"))
my_dict.update({"AAA": 9999, "BBB": True})
print("Deleted value:", my_dict.pop("AAA"), sep=" ")
print("Modified dictionary:", my_dict, sep=" ")
print()

# set type
my_set = {2, 3, 6, 3, True, True, False, "Text", "Text"}
print("Set:", my_set, sep=" ")
my_set.update({9, 10})
my_set.discard(9)
print("Modified set:", my_set, sep=" ")
