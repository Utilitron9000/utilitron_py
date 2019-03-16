import unittest
from .reducer_node import ReducerNode
from ..utility_graph_node import UtilityGraphNode


class TestReducerNode(unittest.TestCase):
    def setUp(self):
        self.nodeA = ReducerNode(lambda x, y: x + y)
        self.nodeB = UtilityGraphNode()
        self.nodeC = UtilityGraphNode()

    def test_get_output(self):
        with self.assertRaises(ValueError):
            self.nodeA.get_output()

        self.nodeB.output_val = 5

        self.nodeA.connect_input(self.nodeB)
        self.assertEqual(self.nodeA.get_output(), 5)
        self.nodeA.reset()

        self.nodeB.output_val = 5
        self.nodeC.output_val = 10

        self.nodeA.connect_input(self.nodeC)
        self.assertEqual(self.nodeA.get_output(), 15)
