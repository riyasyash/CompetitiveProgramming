# Find the missing number from an array of n consecutive integers


class MissingNumberEvaluator:
    def __init__(self, array):
        self._array = array

    def find_missing(self):
        n = self._array[-1]
        expected_sum = (n * (n + 1)) / 2
        actual_sum = sum(self._array)
        missing_number = int(expected_sum - actual_sum)
        return missing_number
