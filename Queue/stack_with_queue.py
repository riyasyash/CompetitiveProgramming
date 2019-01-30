from Queue.Queue import Queue


class Stack:
    def __init__(self):
        self.__queue = Queue()

    def push(self, item):
        self.__queue.enqueue(item)

    def pop(self):
        if self.__queue.length() != 1:
            self.__re_order()
        return self.__queue.dequeue()

    def length(self):
        return self.__queue.length()

    def __re_order(self):
        i = 1
        length = self.__queue.length()
        while i < length:
            self.__queue.enqueue(self.__queue.dequeue())
            i += 1
