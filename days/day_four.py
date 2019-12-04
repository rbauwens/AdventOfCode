def meets_criteria_one(num):
    string_num = str(num)
    len_num = len(string_num)
    double = False
    ascending = True
    for i in range(0, len_num - 1):
        if string_num[i] == string_num[i+1]:
            double = True
        if string_num[i] > string_num[i + 1]:
            ascending = False

    if double and ascending:
        return True
    else:
        return False


def meets_criteria_two(num):
    string_num = str(num)
    len_num = len(string_num)

    double = False
    ascending = True
    for i in range(0, len_num - 1):
        num = string_num[i]
        if string_num.count(num) == 2:
            if string_num[i] == string_num[i+1]:
                double = True
        if string_num[i] > string_num[i + 1]:
            ascending = False

    if double and ascending:
        return True
    else:
        return False


def day_four_part_one():
    passwords = []
    for i in range(357253, 892942):
        if meets_criteria_one(i):
            passwords.append(i)

    return len(passwords)


def day_four_part_two():
    passwords = []
    for i in range(357253, 892942):
        if meets_criteria_two(i):
            passwords.append(i)

    return len(passwords)
