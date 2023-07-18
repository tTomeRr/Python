import math

my_dict = {'apple': 3, 'banana': 2, 'cherry': 4, 'date': 5, 'elderberry': 1, 'pineapple': 3}
my_dict2 = {'jdsya': 3, 'xouat': 5, 'banana': 6, 'hgjri': 1, 'apple': 7}
random_key = "apple"


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


