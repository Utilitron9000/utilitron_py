import unittest
from .average_node import AverageNode
from ..utility_graph_node import UtilityGraphNode

class TestReducerNode(unittest.TestCase):
    def setUp(self):
        self.nodeA = AverageNode()
        self.nodeB = UtilityGraphNode()
        self.nodeB.output_val = 20
        self.nodeC = UtilityGraphNode()
        self.nodeC.output_val = 10

    def test_get_output(self):
        with self.assertRaises(ValueError):
            self.nodeA.get_output()

        self.nodeA.connect_input(self.nodeB)
        self.assertEqual(self.nodeA.get_output(), 20)
        self.nodeA.reset()

        self.nodeA.connect_input(self.nodeC)
        self.assertEqual(self.nodeA.get_output(), 15)

