import unittest
from .utility_graph_node import UtilityGraphNode, NodeConnectionError


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
