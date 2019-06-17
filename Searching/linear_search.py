from Searching.search import Search


class LinearSearch(Search):

    def search(self, search_item):
        for i in range(0, len(self.lot)):
            if self.lot[i] == search_item:
                return True, i
        return False, -1
