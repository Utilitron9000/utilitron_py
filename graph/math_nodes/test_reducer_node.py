import unittest
from graph.math_nodes.reducer_node import ReducerNode
from graph.utility_graph_node import UtilityGraphNode, NodeConnectionError


class TestReducerNode(unittest.TestCase):
    def setUp(self):
        self.nodeA = ReducerNode(lambda x, y: x + y)
        self.nodeB = UtilityGraphNode()
        self.nodeC = UtilityGraphNode()

    def test_output(self):
        with self.assertRaises(NodeConnectionError):
            self.nodeA.output

        self.nodeB._output = 5

        self.nodeA.connect_input(self.nodeB)
        self.assertEqual(self.nodeA.output, 5)
        self.nodeA.reset()

        self.nodeB._output = 5
        self.nodeC._output = 10

        self.nodeA.connect_input(self.nodeC)
        self.assertEqual(self.nodeA.output, 15)
