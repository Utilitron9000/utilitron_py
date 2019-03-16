import unittest
from .stat_node import StatNode


class TestStatNode(unittest.TestCase):
    def setUp(self):
        self.nodeA = StatNode("score")
        self.nodeA.set_value(100)

    def test_reset(self):
        self.assertEqual(self.nodeA.output, 100)
        self.nodeA.reset()
        self.assertEqual(self.nodeA.output, 100)
