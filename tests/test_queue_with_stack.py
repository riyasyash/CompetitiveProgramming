import unittest

from Stack.Queue_with_stack import Queue, QueueEmptyException


class TestQueuewithStack(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()

    def test_queue_init(self):
        self.assertEqual(0, self.queue.length())

    def test_enqueue(self):
        self.queue.enqueue(5)
        self.queue.enqueue(10)
        self.assertEqual(2, self.queue.length())

    def test_dequeue(self):
        self.queue.enqueue(5)
        self.queue.enqueue(10)
        self.assertEqual(5, self.queue.dequeue())
        self.assertEqual(10, self.queue.dequeue())

    def test_dequeue_with_interemittent_enqueu(self):
        self.queue.enqueue(5)
        self.queue.enqueue(10)
        self.assertEqual(5, self.queue.dequeue())
        self.queue.enqueue(15)
        self.assertEqual(10, self.queue.dequeue())
        self.queue.enqueue(20)
        self.assertEqual(15, self.queue.dequeue())

    def test_cannot_dequeue_from_empty_queue(self):
        with self.assertRaises(QueueEmptyException):
            self.queue.dequeue()


if __name__ == '__main__':
    unittest.main()
