import unittest

from Queue.Queue import Queue, QueueEmptyException


class TestQueue(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()

    def test_queue_is_initialised(self):
        self.assertEqual(0, self.queue.length())

    def test_enqueue_is_increasing_length(self):
        self.queue.enqueue(5)
        self.queue.enqueue(10)
        self.assertEqual(2, self.queue.length())

    def test_dequeue_is_reducing_length(self):
        self.queue.enqueue(15)
        self.assertEqual(15, self.queue.dequeue())
        self.assertEqual(0, self.queue.length())

    def test_queue_follows_FIFO(self):
        self.queue.enqueue(20)
        self.queue.enqueue(25)
        self.assertEqual(2, self.queue.length())
        self.assertEqual(20, self.queue.dequeue())

    def test_dequeue_return_error_from_empty_queue(self):
        with self.assertRaises(QueueEmptyException):
            self.queue.dequeue()
