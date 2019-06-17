from Searching.search import Search


class BinarySearch(Search):
    lot_start = 0
    lot_end = 0

    def __int__(self, lot):
        super().__init__(lot=lot)
        self.lot_start = 0
        self.lot_end = len(self.lot)

    def search(self, search_item):
        item, position = self.get_middle_element()
        if item == search_item:
            return True, position

        if item > search_item:
            self.divide(start=self.lot_start, end=position)

        else:
            self.divide(start=position, end=self.lot_end)

        return self.conquer(search_item)

    def get_middle_element(self):
        middle_pos = len(self.lot[self.lot_start:self.lot_end]) // 2
        return self.lot[middle_pos], middle_pos

    def divide(self, start, end):
        self.lot_start = start
        self.lot_end = end

    def conquer(self, search_item):
        if len(self.lot[self.lot_start:self.lot_end]) <= 1:
            return False, -1
        self.search(search_item)
