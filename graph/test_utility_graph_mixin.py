from graph.utility_graph import UtilityGraph
from graph.selection import SelectionMethod
from graph.targetable_action_node import TargetableActionNode
from graph.stat_node import StatNode
from graph.math_nodes.average_node import AverageNode
from graph.math_nodes.inverse_node import InverseNode
from graph.action_node import ActionNode


class TestUtilityGraphMixin:
    def set_up_graph(self):
        self.set_up_eat_action()
        self.set_up_cry_action()
        self.set_up_run_action()

        self.graph = UtilityGraph(5)
        self.graph.top_subset_size = 2
        self.graph.selection_method = SelectionMethod.MAX
        self.graph.actions = {a.id: a for a in [self.eat_action,
                                                self.cry_action,
                                                self.run_action]}

        self.graph.nodes = {n.id: n for n in [self.food_tastiness,
                                              self.food_distance]}

    def set_up_eat_action(self):
        self.eat_action = TargetableActionNode('eat')

        self.hunger = StatNode('hunger')
        self.hunger.set_value(0.5)

        self.food_distance = StatNode('food_distance')
        self.fd_inv = InverseNode()
        self.fd_inv.connect_input(self.food_distance)

        self.food_tastiness = StatNode('food_tastiness')

        self.eat_avg = AverageNode()
        self.eat_avg.connect_input(self.hunger)
        self.eat_avg.connect_input(self.fd_inv)
        self.eat_avg.connect_input(self.food_tastiness)
        self.eat_action.connect_input(self.eat_avg)

        self.eat_action_targets = [
            {
                'key': 'pickle',
                'food_distance': 0.2,
                'food_tastiness': 0.05,
            },
            {
                'key': 'cake',
                'food_distance': 0.5,
                'food_tastiness': 1.0
            },
            {
                'key': 'apple',
                'food_distance': 0.3,
                'food_tastiness': 0.7
            },
        ]

    def set_up_cry_action(self):
        self.cry_action = ActionNode('cry')
        self.sadness = StatNode('sadness')
        self.cry_action.connect_input(self.sadness)
        self.sadness.set_value(1.0)

    def set_up_run_action(self):
        self.run_action = ActionNode('run')
        self.energy = StatNode('energy')
        self.run_action.connect_input(self.energy)
        self.energy.set_value(0.3)
