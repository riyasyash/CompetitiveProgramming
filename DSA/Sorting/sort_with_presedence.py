# 54


class SortWithPrecedence:
    def __init__(self, list_one, list_two):
        self._list_one = list_one
        self._list_two = list_two
        self.sorted = []

    def sort(self):
        self._list_one = sorted(self._list_one)
        for item in self._list_two:
            while item in self._list_one:
                self.sorted.append(item)
                self._list_one.remove(item)
        self.sorted.extend(self._list_one)
        return  self.sorted
