from typing import Dict, Tuple, Callable
from graph.utility_graph_node import UtilityGraphNode
from graph.action_node import ActionNode
from graph.targetable_action_node import TargetableActionNode, TargetStats
from graph.selection import select_weighted_random, SelectionMethod
from graph.exceptions import NodeNotFoundError, NodeTypeError

ActionKV = Tuple[str, ActionNode]


class UtilityGraph:
    def __init__(self, seed):
        self.nodes: Dict[str, UtilityGraphNode] = {}
        self.actions: Dict[str, ActionNode] = {}
        self.selection_method: SelectionMethod = SelectionMethod.MAX
        self.top_subset_size: int = 3
        self.utility_key: Callable = lambda kv: kv[1].output

    def update_targets(self, action_name: str, targets: TargetStats):
        """Finds a targetable action node and updates it with the
        target stats related to that action"""
        if action_name not in self.actions:
            raise NodeNotFoundError('Cannot find action in graph')

        action_node = self.actions[action_name]
        if not isinstance(action_node, TargetableActionNode):
            raise NodeTypeError('Cannot update targets for a node \
            that is not a TargetableActionNode')

        action_node.verify_targets(targets, self.nodes)
        action_node.targets = targets

    def get_next_action(self) -> ActionNode:
        """Get the next action the agent should take based
        on the current game stats. Returns the action id"""
        if not self.actions:
            return None

        self._reset_all_nodes()

        best_action = {
            SelectionMethod.MAX: self._max_selection,
            SelectionMethod.WEIGHTED_RANDOM: self._weighted_random_selection,
        }

        return best_action[self.selection_method]()

    def _reset_all_nodes(self):
        """Reset all nodes in the graph, setting
        the output value to None for all nodes
        except GameStat and Constant nodes"""
        for id, action in self.actions.items():
            action.reset()

    def _max_selection(self):
        """Selects the action with the highest utility value"""
        return max(self.actions.items(), key=self.utility_key)[1]

    def _weighted_random_selection(self) -> Tuple[str, float]:
        """Performs a weighted random selection on the 'top_subset_size' actions with
        the highest utility values."""
        return select_weighted_random(self.actions.items(),
                                      self.top_subset_size,
                                      self.utility_key)[1]
