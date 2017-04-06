def find_missing(array1, array2):
    if isinstance(array1, list):
        if isinstance(array2, list):
            if_array_identical = 0
            if set(array1) == set(array2):
                return if_array_identical
            else:
                result = list(set(array1) ^ set(array2))
                return result[0]

        else:
            return "Second argument is not an array"
    else:
        return "First argument is not an array"
