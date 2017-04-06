class BinarySearch(list):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        for i in range(1, a+1):
            self.append(i*b)
        self.length = len(self)

    def search(self, term):
        binary_search_result = {}
        counter = 0
        start_point = 0
        end_point = (self.length - 1)
        if self[end_point] == term:
            binary_search_result["index"] = end_point
            binary_search_result["count"] = counter
            return binary_search_result
        if self[start_point] == term:
            binary_search_result["index"] = start_point
            binary_search_result["count"] = counter
            return binary_search_result

        while start_point < end_point:
            mid_point = (start_point + end_point) // 2

            if self[mid_point] == term:
                binary_search_result["index"] = mid_point
                binary_search_result["count"] = counter
                return binary_search_result

            elif self[mid_point] < term:
                start_point = mid_point + 1
            elif self[mid_point] > term:
                end_point = mid_point - 1
            counter += 1
            binary_search_result["index"] = -1
            binary_search_result["count"] = counter - 1
        return binary_search_result
