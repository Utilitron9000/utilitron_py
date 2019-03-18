import unittest
import math
from graph.targetable_action_node import TargetableActionNode
from graph.test_utility_graph_mixin import TestUtilityGraphMixin
from graph.exceptions import NodeTypeError, NodeNotFoundError


class TestTargetableActionNode(unittest.TestCase, TestUtilityGraphMixin):
    def setUp(self):
        self.set_up_graph()
        self.new_node = TargetableActionNode('attack')
        self.graph.nodes[self.new_node.id] = self.new_node

        self.hunger.set_value(0.5)
        self.graph.update_targets('eat', self.eat_action_targets)
        self.target_utilities = self.eat_action._get_target_utilities()

    def test_get_output(self):
        self.assertEqual(self.new_node.output, -math.inf)

    def test_verify_target_stats(self):
        inconsistent_stat_names_A = [
            {
                'a': 0,
                'b': 1
            },
            {
                'b': 1
            },
        ]
        with self.assertRaises(ValueError):
            self.new_node._verify_target_stats(inconsistent_stat_names_A, self.graph.nodes)

        inconsistent_stat_names_B = [
            {
                'b': 1
            },
            {
                'a': 0,
                'b': 1
            },
        ]
        with self.assertRaises(ValueError):
            self.new_node._verify_target_stats(inconsistent_stat_names_B, self.graph.nodes)

        stat_not_in_graph = [
            {
                'food_distance': 0.5,
                'food_tastiness': 0.5,
                'a': 0,
            },
            {
                'food_distance': 0.5,
                'food_tastiness': 0.5,
                'a': 0,
            },
        ]

        with self.assertRaises(NodeNotFoundError):
            self.new_node._verify_target_stats(stat_not_in_graph, self.graph.nodes)

        node_not_stat_type = [
            {
                'food_distance': 0.5,
                'food_tastiness': 0.5,
                'attack': 0,
            },
            {
                'food_distance': 0.5,
                'food_tastiness': 0.5,
                'attack': 0,
            },
        ]
        with self.assertRaises(NodeTypeError):
            self.new_node._verify_target_stats(node_not_stat_type, self.graph.nodes)

    def test_get_target_utilities(self):
        eat_pickle, eat_cake, eat_apple = self.target_utilities
        self.assertAlmostEqual(eat_pickle, (0.8 + 0.05 + 0.5) / 3)
        self.assertAlmostEqual(eat_cake, (0.5 + 1.0 + 0.5) / 3)
        self.assertAlmostEqual(eat_apple, (0.7 + 0.7 + 0.5) / 3)

    def test_max_selection(self):
        self.assertEqual(self.eat_action._max_selection(self.target_utilities),
                         (0.5 + 1.0 + 0.5) / 3)
