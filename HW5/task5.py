lst = [45,5,6,45,2,15,1,85,2,6,75]
print(*lst)

list_unique = list(set(lst))
print(*list_unique)

is_all_unique = len(lst) == len(list_unique)
print(f"All unique: {is_all_unique}")

if is_all_unique == False:
    dict_duplicates = [{x: lst.count(x)} for x in list_unique if lst.count(x) > 1]
    print(*dict_duplicates)
