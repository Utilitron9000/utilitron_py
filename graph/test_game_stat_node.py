import unittest
from .game_stat_node import GameStatNode
from .utility_graph_node import UtilityGraphNode

class TestGameStatNode(unittest.TestCase):
    def setUp(self):
        self.nodeA = GameStatNode("score")
        self.nodeA.set_value(100)

    def test_reset(self):
        self.assertEqual(self.nodeA.get_output(), 100)
        self.nodeA.reset()
        self.assertEqual(self.nodeA.get_output(), 100)
