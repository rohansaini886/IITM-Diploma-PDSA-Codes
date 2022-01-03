def odd_one(l):
    my_dict = {'int': 0, 'float': 0, 'str': 0, 'bool': 0}
    for i in l:
        if type(i) == int:
            my_dict['int'] += 1
        if type(i) == float:
            my_dict['float'] += 1
        if type(i) == str:
            my_dict['str'] += 1
        if type(i) == bool:
            my_dict['bool'] += 1
    for t, count in my_dict.items():
        if count == 1:
            return t
print(odd_one(eval(input().strip())))
