class Stack():
    """
    This is a simple implementation of Stack
    """
    pass

    def __init__(self):
        self.__items = []

    def push(self, item):
        self.__items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.__items.pop()
        raise StackEmptyException('stack is empty')

    def length(self):
        return len(self.__items)

    def is_empty(self):
        if not len(self.__items):
            return True
        return False


class StackEmptyException(Exception):
    pass
