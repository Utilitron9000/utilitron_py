import unittest
from graph.math_nodes.inverse_node import InverseNode
from graph.utility_graph_node import UtilityGraphNode
from graph.exceptions import NodeConnectionError


class TestInverseNode(unittest.TestCase):
    def setUp(self):
        self.nodeA = InverseNode()
        self.nodeB = UtilityGraphNode()

    def test_output(self):
        with self.assertRaises(NodeConnectionError):
            self.nodeA.output

        self.nodeB._output = 0.7
        self.nodeA.connect_input(self.nodeB)
        self.assertAlmostEqual(self.nodeA.output, 0.3)
        self.nodeA.reset()

        self.nodeB._output = 0.5
        self.assertAlmostEqual(self.nodeA.output, 0.5)
        self.nodeA.reset()

        self.nodeB._output = 4
        self.assertAlmostEqual(self.nodeA.output, 0)
        self.nodeA.reset()
