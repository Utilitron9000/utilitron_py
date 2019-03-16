import unittest
from .utility_graph import UtilityGraph, SelectionMethod
from .action_node import ActionNode
from .game_stat_node import GameStatNode


class TestUtilityGraph(unittest.TestCase):
    def setUp(self):
        self.graph = UtilityGraph(5)
        self.graph.top_subset_size = 2
        self.graph.selection_method = SelectionMethod.MAX

        self.actionA = ActionNode('eat')
        self.hunger = GameStatNode('hunger')
        self.actionA.connect_input(self.hunger)

        self.actionB = ActionNode('cry')
        self.sadness = GameStatNode('sadness')
        self.actionB.connect_input(self.sadness)

        self.actionC = ActionNode('run')
        self.energy = GameStatNode('energy')
        self.actionC.connect_input(self.energy)

        self.actionD = ActionNode('jump')
        self.actionD.connect_input(self.energy)

        self.graph.actions = {a.id: a for a in [self.actionA,
                                                self.actionB,
                                                self.actionC,
                                                self.actionD]}

    def test_max_selection(self):
        self.hunger.set_value(0.5)
        self.sadness.set_value(1.0)
        self.energy.set_value(0.3)

        action = self.graph.get_next_action()
        self.assertEqual(action.name, 'cry')

        self.sadness.set_value(0.2)
        action = self.graph.get_next_action()
        self.assertEqual(action.name, 'eat')

    def test_get_top_actions(self):
        self.hunger.set_value(0.5)
        self.sadness.set_value(1.0)
        self.energy.set_value(0.3)

        top_actions = self.graph._get_top_actions()
        self.assertEqual(len(top_actions), 2)
        for a in top_actions:
            self.assertTrue(a[1].name in ['eat', 'cry'])
            self.assertFalse(a[1].name in ['run', 'jump'])

    def test_weight_actions(self):
        self.hunger.set_value(0.5)
        self.sadness.set_value(1.0)
        self.energy.set_value(0.3)

        top_actions = self.graph._get_top_actions()
        weighted = self.graph._weight_actions_by_utility(top_actions)

        self.assertEqual(len([kv for kv in weighted
                              if kv[1].name == 'cry']), 100)

        self.assertEqual(len([kv for kv in weighted
                              if kv[1].name == 'eat']), 50)
