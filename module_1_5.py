# module_1_5.py

# var assignment by tuple type
immutable_var = (1, "Text", True, [0, 1], {1: "Data"})
print("Immutable tuple:", end=" ")
print(immutable_var, immutable_var[2], immutable_var[:3], sep="  |  ")

# immutable_var[0] = "aaa"  # will be error
# tuple type is immutable

# var assignment by list type
mutable_list = [1, "Text", False]
mutable_list[1] = "New Text"
print("Mutable list:", mutable_list, sep=" ")
