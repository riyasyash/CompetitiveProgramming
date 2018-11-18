from Stack.Stack import Stack, StackEmptyException


class QueueEmptyException(Exception):
    pass


class Queue():
    """
    An implementation of Queue with two Stacks
    """
    def __init__(self):
        self.__in_stack = Stack()
        self.__out_stack = Stack()

    def length(self):
        return self.__in_stack.length() + self.__out_stack.length()

    def enqueue(self, item):
        self.__in_stack.push(item)

    def is_empty(self):
        return self.__out_stack.is_empty() and self.__in_stack.is_empty()

    def dequeue(self):
        if self.is_empty():
            raise QueueEmptyException('Queue is empty')
        if self.__out_stack.is_empty():
            self._re_fill_out_stack()
        try:
            return self.__out_stack.pop()
        except StackEmptyException:
            raise QueueEmptyException('Queue is empty')

    def _re_fill_out_stack(self):
        while (self.__in_stack.length()):
            self.__out_stack.push(self.__in_stack.pop())
