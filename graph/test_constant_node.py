import unittest
from .constant_node import ConstantNode
from .utility_graph_node import UtilityGraphNode

class TestGameStatNode(unittest.TestCase):
    def setUp(self):
        self.nodeA = ConstantNode(100)

    def test_set_value(self):
        self.assertEqual(self.nodeA.get_output(), 100)
        self.nodeA.set_value(50)
        self.assertEqual(self.nodeA.get_output(), 50)

    def test_reset(self):
        self.assertEqual(self.nodeA.get_output(), 100)
        self.nodeA.reset()
        self.assertEqual(self.nodeA.get_output(), 100)
