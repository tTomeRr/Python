def q1():
    number = lambda x: x + 15
    print(number(5))


def q3(my_list):
    sorted_list = sorted(my_list, key=lambda x: x[1], reverse=True)
    return sorted_list

def q4(my_dict):
    return sorted(my_dict, key=lambda x: x[1])
