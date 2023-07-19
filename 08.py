import datetime

my_list = [1, 2, 3, 4, 5, 7, 6, 0, -2, -4, 13]
another_list = ["abc", "Dva", "pubg", "Pubg", "RL", "rl"]

def q1():
    number = lambda x: x + 15
    print(number(5))


def q3(my_list):
    sorted_list = sorted(my_list, key=lambda x: x[1], reverse=True)
    return sorted_list

def q4(my_dict):
    return sorted(my_dict, key=lambda x: x[1])

def q5():
    my_list = [5, 23, 12, 6, 10, 43, 34, 96, 15]
    even = lambda x : x % 2 == 0
    new_list = list(filter(even, my_list))
    print(new_list)

def q6(my_list):
    square_list = list(map(lambda x : x**2, my_list))
    cube_list = list(map(lambda x: x ** 3, my_list))
    print(square_list)
    print(cube_list)

def q7(string, character):
    start = lambda x: True if x.startswith(character) else False

def q8():
    now = datetime.datetime.now()
    year = lambda x : x.year
    month = lambda x : x.month
    day = lambda x : x.day
    time = lambda x : x.time()
    print("{}/{}/{} {}".format(day(now), month(now), year(now), time(now)))

def q9(string):
    is_str = lambda x : isinstance(x, str)
    print(is_str(string))

def q11(ls1, ls2):
    intersection = set(filter(lambda x : x in ls1, ls2))
    print(intersection)

def q12(array):
    new_array = sorted(array, key=lambda x : x, reverse=True)
    print(new_array)

def q13(my_list):
    pos = len(list(filter(lambda x : x > 0, my_list)))
    neg = len(list(filter(lambda x: x < 0, my_list)))
    print("positive: {} negative: {}".format(pos, neg))

def q14(my_list):
    len6 = list(filter(lambda x : len(x) > 6, my_list))
    print(len6)

def q15(list1, list2):
    new_list = list(map(lambda x,y : x+y, list1, list2))
    print(new_list)

def q16():
    students = []
    num_of_students = int(input("Enter number of students: "))
    for i in range(num_of_students):
        name = input("Enter name: ")
        grade = int(input("Enter grade: "))
        students.append([name, grade])
    print("All students: \n{}".format(students))
    students = sorted(students, key=lambda x : x[1])
    print(students[1])

def q17(my_list):
    new_list = list(filter(lambda x : x % 13 == 0 or x % 19 == 0, my_list))
    print(new_list)

def q18(my_list):
    new_list = list(filter(lambda x : str(x) == str(x)[::-1], my_list))
    print(new_list)

def q19(string, list1):
    print("?")

def q20(my_list):
    only_num = list(filter(lambda x : isinstance(x, int), my_list))
    only_num = sorted(list(filter(lambda x : x > len(only_num), only_num)))
    print(only_num)

def q21(my_list, number):
    my_list = list(map(lambda x : x * number, my_list))
    print(my_list)

def q22(my_list):
    my_list = sum(map(lambda x : len(x), list(filter(lambda x : not x[0].islower(), my_list))))
    print(my_list)

def q23(my_list):
    return q13(my_list)

def sum_digits(number):
    if number == 0:
        return 0
    else:
        return number % 10 + sum_digits(int(number / 10))
def q24(rng):
    for i in range(1, rng):
        if i % sum_digits(i) == 0:
            print(i, end=", ")


def q25(number):
    number_list = [int(digit) for digit in str(number)]
    for i in range(len(number_list) - 1):
        if number_list[i] < number_list[i+1]:
            number_list[i], number_list[i+1] = number_list[i+1], number_list[i]
            return int(''.join(str(digit) for digit in number_list))
    return 0
