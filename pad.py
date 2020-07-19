# python


def sum_values(arr):
    result = 0
    for i in arr:
        if check_isstring(i):
            if check_isnumeric(i):
                result += int(i)
            else:
                pass
        else:
            result += i

    return result


def check_isstring(var):
    if type(var) == str:
        return True
    else:
        return False


def check_isnumeric(var):
    return var.isnumeric()


test_array = [7.5, 1, 2, 5, 'k', '7']

print(sum_values(test_array))

