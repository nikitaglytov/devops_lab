def myfunc(keys, values):
    result = dict.fromkeys(keys, None)
    result.update(zip(keys, values))
    return result

print(myfunc({1, 2, 3}, {'abc', 'zbx'}))
