import unittest
from .score_node import ScoreNode
from .utility_graph_node import UtilityGraphNode


class TestScoreNode(unittest.TestCase):
    def setUp(self):
        self.nodeA = ScoreNode("name")
        self.nodeB = UtilityGraphNode()
        self.nodeB._UtilityGraphNode__output = 5

    def test_get_output(self):
        self.assertEqual(self.nodeA.output, None)
        self.nodeA.connect_input(self.nodeB)
        self.assertEqual(self.nodeA.output, 5)
