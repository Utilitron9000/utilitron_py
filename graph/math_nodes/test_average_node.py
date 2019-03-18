import unittest
from graph.math_nodes.average_node import AverageNode
from graph.utility_graph_node import UtilityGraphNode


class TestAverageNode(unittest.TestCase):
    def setUp(self):
        self.nodeA = AverageNode()
        self.nodeB = UtilityGraphNode()
        self.nodeC = UtilityGraphNode()

    def test_output(self):
        self.nodeB._output = 20

        self.nodeA.connect_input(self.nodeB)
        self.assertEqual(self.nodeA.output, 20)
        self.nodeA.reset()

        self.nodeB._output = 20
        self.nodeC._output = 10

        self.nodeA.connect_input(self.nodeC)
        self.assertEqual(self.nodeA.output, 15)
