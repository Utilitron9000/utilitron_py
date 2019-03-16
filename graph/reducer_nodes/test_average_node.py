import unittest
from .average_node import AverageNode
from ..utility_graph_node import UtilityGraphNode


class TestReducerNode(unittest.TestCase):
    def setUp(self):
        self.nodeA = AverageNode()
        self.nodeB = UtilityGraphNode()
        self.nodeC = UtilityGraphNode()

    def test_output(self):
        self.nodeB._UtilityGraphNode__output = 20

        self.nodeA.connect_input(self.nodeB)
        self.assertEqual(self.nodeA.output, 20)
        self.nodeA.reset()

        self.nodeB._UtilityGraphNode__output = 20
        self.nodeC._UtilityGraphNode__output = 10

        self.nodeA.connect_input(self.nodeC)
        self.assertEqual(self.nodeA.output, 15)


