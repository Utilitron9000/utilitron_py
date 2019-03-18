import unittest
from graph.selection import get_top_x, get_weighted
from graph.exceptions import NodeNotFoundError, NodeTypeError
from graph.test_utility_graph_mixin import TestUtilityGraphMixin


class TestUtilityGraph(unittest.TestCase, TestUtilityGraphMixin):
    def setUp(self):
        self.set_up_graph()

    def test_update_targets(self):
        with self.assertRaises(NodeNotFoundError):
            self.graph.update_targets('nonexistent_action', {})

        with self.assertRaises(NodeTypeError):
            self.graph.update_targets('cry', {})

        self.sadness.set_value(0.5)
        self.hunger.set_value(0.5)

        self.graph.update_targets('eat', self.eat_action_targets)

        action = self.graph.get_next_action()
        self.assertEqual(action.name, 'eat')
        self.assertEqual(action.target_index, 1)

    def test_max_selection(self):
        action = self.graph.get_next_action()
        self.assertEqual(action.name, 'cry')

        self.sadness.set_value(0.2)
        action = self.graph.get_next_action()
        self.assertEqual(action.name, 'run')

    def test_get_top_actions(self):
        top_actions = get_top_x(self.graph.actions.items(),
                                self.graph.top_subset_size,
                                self.graph.utility_key)
        self.assertEqual(len(top_actions), 2)

        for a in top_actions:
            self.assertTrue(a[1].name in ['cry', 'run'])
            self.assertFalse(a[1].name in ['eat'])

    def test_weight_actions(self):
        top_actions = get_top_x(self.graph.actions.items(),
                                self.graph.top_subset_size,
                                self.graph.utility_key)
        weighted = get_weighted(top_actions, self.graph.utility_key)

        self.assertEqual(len([kv for kv in weighted
                              if kv[1].name == 'cry']), 100)

        self.assertEqual(len([kv for kv in weighted
                              if kv[1].name == 'run']), 30)
