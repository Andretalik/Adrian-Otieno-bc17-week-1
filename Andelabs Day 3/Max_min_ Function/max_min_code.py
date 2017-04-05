def find_max_min(number_array):
    if isinstance(number_array, list):
        if len(set(number_array)) <= 1:
            fail_list = [len(number_array)]
            return fail_list
        else:
            maximum = max(number_array)
            minimum = min(number_array)
            result_list = [minimum, maximum]
            return result_list
    else:
        return "Only lists allowed"
