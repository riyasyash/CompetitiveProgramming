class Queue:
    def __init__(self):
        self.__items = []

    def enqueue(self, item):
        self.__items.append(item)

    def dequeue(self):
        if not self.length():
            raise QueueEmptyException()
        item = self.__items[0]
        self.__items = self.__items[1:]
        return item

    def length(self):
        return len(self.__items)


class QueueEmptyException(Exception):
    pass
