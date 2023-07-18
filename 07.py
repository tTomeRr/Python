import math

my_dict = {'apple': 3, 'banana': 2, 'cherry': 4, 'date': 5, 'elderberry': 1, 'pineapple': 3}
my_dict2 = {'jdsya': 3, 'xouat': 5, 'banana': 6, 'hgjri': 1, 'apple': 7}
random_key = "apple"
my_list = [1, 5, 3]


def q1(my_dict):
    asc_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))
    print("Dictionary is asc order: {}".format(asc_dict))
    dec_dict = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
    print("Dictionary is dec order: {}".format(dec_dict))


def q2(my_dict, key_to_add):
    print("Dictionary before adding: {}".format(my_dict))
    my_dict.update(key_to_add)
    print("Dictionary after adding: {}".format(my_dict))


def q3(my_dict, my_dict2):
    my_dict.update(my_dict2)
    print("New dictionary: {}".format(my_dict))


def q4(my_dict, key_to_find):
    return key_to_find in my_dict.keys()


def q5(my_dict):
    for key, value in my_dict.items():
        print("{} : {}".format(key, value))


def q6(n):
    my_dict = {i: i * i for i in range(1, n + 1)}
    print(my_dict)


def q7():
    my_dict = {i: i * i for i in range(1, 16)}
    print(my_dict)


def q8(my_dict, my_dict2):
    q3(my_dict, my_dict2)


def q9(my_dict):
    q5(my_dict)


def q10(my_dict):
    return sum(value for value in my_dict.values() if isinstance(value, int))


def q11(my_dict):
    return math.prod(value for value in my_dict.values() if isinstance(value, int))


def q12(my_dict, key_to_remove):
    if key_to_remove in my_dict.keys():
        my_dict.pop(key_to_remove)
        print(my_dict)
    else:
        print("Key not in dictionary.")


def q13(list1, list2):
    my_dict = {list1[i]: list2[i] for i in range(len(list1))}
    print(my_dict)


def q14(my_dict):
    return dict(sorted(my_dict.items()))


def q15(my_dict):
    maxN = max(value for value in my_dict.values())
    minN = min(value for value in my_dict.values())
    print("max: {}, min: {}".format(maxN, minN))


def q16(objectt):
    return vars(objectt)


def q17(my_dict):
    temp = {}
    for key, value in my_dict.items():
        if value not in temp.values():
            temp.update({key: value})
    return temp


def q18(my_dict):
    return "Not empty" if bool(my_dict) else "Empty"


def q19(my_dict, my_dict2):
    res = {}
    for key, value in my_dict.items():
        if key not in res:
            res[key] = 0
            res[key] += value
        else:
            res[key] += value

    for key, value in my_dict2.items():
        if key not in res:
            res[key] = 0
            res[key] += value
        else:
            res[key] += value
    return res


def q20(my_dict):
    res = {}
    for key, value in my_dict.items():
        if value not in res.values():
            res.update({key: value})
    return res.values()


def q21(my_dict):
    values = list(my_dict.values())
    for letter1 in values[0]:
        for letter2 in values[1]:
            print(letter1 + letter2)


def q22(my_dict):
    sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
    keys = list(sorted_dict.keys())[:3]
    values = list(sorted_dict.values())[:3]
    print({keys[i]: values[i] for i in range(len(keys))})


def q23(my_list):
    temp = {}
    temp_list = []
    for dic in my_list:
        for value in dic.values():
            temp_list.append(value)
    for i in range(0, len(temp_list), 2):
        if temp_list[i] not in temp.keys():
            temp[temp_list[i]] = temp_list[i + 1]
        else:
            temp[temp_list[i]] += temp_list[i + 1]
    print(temp)


def q24(my_dict):
    return "".join(key * value for key, value in my_dict.items())


def q25(my_dict):
    for key, value in my_dict.items():
        print(f'{key: <10}    {value: <15}')


def q26():
    data = [
        {'id': 1, 'success': True, 'name': 'Lary'},
        {'id': 2, 'success': False, 'name': 'Rabi'},
        {'id': 3, 'success': True, 'name': 'Alex'}
    ]
    success = 0
    for dic in data:
        if dic['success']:
            success += 1
    print(success)


def q27(my_list):
    my_dic = {str(key): 0 for key in my_list}
    print(my_dic)


def q28():
    print("???????????????")


def q29(my_dict):
    no_space = {}
    for key, value in my_dict.items():
        temp = key
        temp = temp.replace(" ", "")
        no_space[temp] = value
    print(no_space)


def q30(my_dict):
    sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
    keys = list(sorted_dict.keys())[:3]
    values = list(sorted_dict.values())[:3]
    print({keys[i]: values[i] for i in range(len(keys))})


def q31(my_dict):
    print(my_dict)


def q32(my_dict):
    for key, value in my_dict.items():
        print("{}: {}".format(key, value))


def q33():
    print("??????")


def q34(my_dict):
    count = 0
    for value in my_dict.values():
        if isinstance(value, list):
            count += 1
    print(count)


def q35(my_dict):
    return dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))


def q36(list1, list2):
    return {list1[i]: list2[i] for i in range(len(list1))}


def q37(my_dict):
    avg = sum(value for value in my_dict.values()) / len(my_dict)
    for key in my_dict.keys():
        my_dict[key] = avg
    print(my_dict)


def q38(my_dict, my_dict2):
    return q19(my_dict, my_dict2)


def q39():
    print("???")


def q40():
    my_dict = {'x': 0, 'y': 0, 'z': 0}
    i = 11
    for key in my_dict.keys():
        my_dict[key] = [i + n for n in range(9)]
        i += 10
    print(my_dict)


def q41(my_dict):
    return {key: value for key, value in my_dict.items() if value is not None}


def q42(my_dict, min_value):
    return {key: value for key, value in my_dict.items() if value > min_value}
