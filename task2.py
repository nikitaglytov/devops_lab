list1 = ["a", "b", "c", "d"]
list2 = [1, 2, 3]


def myfunc(keys, values):
    result = dict.fromkeys(keys, None)
    result.update(zip(keys, values))
    return result


print(myfunc(list1, list2))
