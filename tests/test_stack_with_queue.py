import unittest

from Queue.stack_with_queue import Stack


class TestStackWithQueue(unittest.TestCase):
    def setUp(self):
        self.Stack = Stack()

    def test_length_of_the_initialised_stack_is_zero(self):
        self.assertEqual(0, self.Stack.length())

    def test_push_increases_the_length(self):
        self.Stack.push(5)
        self.assertEqual(1, self.Stack.length())
        self.Stack.push(10)
        self.assertEqual(2, self.Stack.length())

    def test_pop_reduces_size(self):
        self.Stack.push(5)
        self.Stack.push(10)
        self.assertEqual(2, self.Stack.length())
        self.Stack.pop()
        self.assertEqual(1, self.Stack.length())

    def test_pop_gives_the_top(self):
        self.Stack.push(5)
        self.Stack.push(10)
        self.assertEqual(2, self.Stack.length())
        self.assertEqual(10, self.Stack.pop())

    def test_intermittent_operations_are_successful(self):
        self.Stack.push(5)
        self.Stack.push(10)
        self.assertEqual(10, self.Stack.pop())
        self.Stack.push(15)
        self.Stack.push(20)
        self.assertEqual(20, self.Stack.pop())
        self.assertEqual(15, self.Stack.pop())
        self.assertEqual(5, self.Stack.pop())
        self.Stack.push(50)
        self.assertEqual(50, self.Stack.pop())
