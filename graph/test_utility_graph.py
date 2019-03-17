import unittest
from graph.utility_graph import UtilityGraph
from graph.selection import SelectionMethod
from graph.action_node import ActionNode
from graph.targetable_action_node import TargetableActionNode
from graph.stat_node import StatNode
from graph.selection import get_top_x, get_weighted
from graph.exceptions import NodeNotFoundError, NodeTypeError
from graph.math_nodes.average_node import AverageNode
from graph.math_nodes.inverse_node import InverseNode


class TestUtilityGraph(unittest.TestCase):
    def setUp(self):
        self.graph = UtilityGraph(5)
        self.graph.top_subset_size = 2
        self.graph.selection_method = SelectionMethod.MAX

        self.eat_action = TargetableActionNode('eat')

        self.hunger = StatNode('hunger')

        self.food_distance = StatNode('food_distance')
        self.fd_inv = InverseNode()
        self.fd_inv.connect_input(self.food_distance)

        self.food_tastiness = StatNode('food_tastiness')

        self.eat_avg = AverageNode()
        self.eat_avg.connect_input(self.hunger)
        self.eat_avg.connect_input(self.fd_inv)
        self.eat_avg.connect_input(self.food_tastiness)
        self.eat_action.connect_input(self.eat_avg)

        self.cry_action = ActionNode('cry')
        self.sadness = StatNode('sadness')
        self.cry_action.connect_input(self.sadness)

        self.run_action = ActionNode('run')
        self.energy = StatNode('energy')
        self.run_action.connect_input(self.energy)

        self.graph.actions = {a.id: a for a in [self.eat_action,
                                                self.cry_action,
                                                self.run_action]}

        self.graph.nodes = {n.id: n for n in [self.food_tastiness,
                                              self.food_distance]}

        self.hunger.set_value(0.5)
        self.sadness.set_value(1.0)
        self.energy.set_value(0.3)

    def test_update_targets(self):
        with self.assertRaises(NodeNotFoundError):
            self.graph.update_targets('nonexistent_action', {})

        with self.assertRaises(NodeTypeError):
            self.graph.update_targets('cry', {})

        self.sadness.set_value(0.5)

        targets = [
            {
                'name': 'pickle',
                'food_distance': 0.2,
                'food_tastiness': 0.05,
            },
            {
                'name': 'cake',
                'food_distance': 0.5,
                'food_tastiness': 1.0
            },
            {
                'name': 'apple',
                'food_distance': 0.3,
                'food_tastiness': 0.7
            },
        ]

        target_stats = {'food_distance': [], 'food_tastiness': []}
        for t in targets:
            for k, v in t.items():
                if k in target_stats:
                    target_stats[k].append(v)

        self.graph.update_targets('eat', target_stats)

        action = self.graph.get_next_action()
        self.assertEqual(action.name, 'eat')
        self.assertEqual(action.num_targets, 3)
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
