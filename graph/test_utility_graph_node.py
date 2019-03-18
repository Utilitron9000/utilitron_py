import unittest
from graph.utility_graph_node import UtilityGraphNode
from graph.exceptions import NodeConnectionError


class TestUtilityGraphNode(unittest.TestCase):
    def setUp(self):
        self.nodeA = UtilityGraphNode()
        self.nodeB = UtilityGraphNode()
        self.nodeC = UtilityGraphNode()

    def test_get_output(self):
        self.assertEqual(self.nodeA.output, None)

    def test_connect_input(self):
        self.nodeA.connect_input(self.nodeB)

        with self.assertRaises(NodeConnectionError):
            self.nodeA.connect_input(self.nodeC)
