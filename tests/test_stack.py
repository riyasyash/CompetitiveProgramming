import unittest

from Stack.Stack import Stack, StackEmptyException


class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_stack_init(self):
        self.assertEqual(0, self.stack.length())

    def test_stack_push(self):
        self.stack.push(5)
        self.assertEqual(1, self.stack.length())

    def test_stack_pop(self):
        self.stack.push(5)
        self.stack.push(10)
        self.assertEqual(10, self.stack.pop())
        self.assertEqual(5, self.stack.pop())
        self.assertEqual(0, self.stack.length())

    def test_cannot_pop_from_empty_stack(self):
        with self.assertRaises(StackEmptyException):
            self.stack.pop()

    def test_is_stack_empty_returns_true_for_empty_stack(self):
        self.assertEqual(True, self.stack.is_empty())


