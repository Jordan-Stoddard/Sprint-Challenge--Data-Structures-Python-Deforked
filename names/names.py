import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

"""
We take in two lists then convert those lists in to sets (sets are essentially hash tables).
We then check to see if we were to run an intersection, if the length of that intersection is greater than 0, 
if it is, it means there are duplicates,
in which case we should return those duplicates, else return None.

Under the hood, set.intersection() is doing a single for loop, doing a check on each item in set_1:

result = set()
for i in set_1:
    if set_1[i] in set_2:
        result.add(set_1[i])
return result

We can do the check if i in set_2 with lightning fast efficiency because sets are non-indexed,
and therefore do not have to be iterated through to check if a matching string is contained.
"""
def names_in_common(list1, list2):
    set_1 = set(list1)
    set_2 = set(list2)

    if len(set_1.intersection(set_2)) > 0:
        return(set_1.intersection(set_2))

duplicates = names_in_common(names_1, names_2)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")


# duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)



