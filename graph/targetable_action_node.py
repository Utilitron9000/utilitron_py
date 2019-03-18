import math
from typing import Dict, List
from graph.action_node import ActionNode
from graph.stat_node import StatNode
from graph.selection import select_weighted_random, SelectionMethod
from graph.utility_graph_node import UtilityGraphNode
from graph.exceptions import NodeNotFoundError, NodeTypeError

TargetStats = List[Dict[str, float]]


class TargetableActionNode(ActionNode):
    """Node representing a possible action available to an agent
    that can be performed on a number of different target_stats"""
    def __init__(self, name: str):
        ActionNode.__init__(self, name)
        self.__targets: TargetStats = {}
        self.stat_nodes: Dict[str, StatNode] = {}
        self.num_targets: int = 0
        self.target_index: int = -1
        self.top_subset_size: int = 3
        self.selection_method: SelectionMethod = SelectionMethod.MAX

    @property
    def targets(self):
        return self.__targets

    @targets.setter
    def targets(self, targets):
        self.__targets = targets
        if not targets:
            self.target_index = -1

    @ActionNode.output.getter
    def output(self) -> float:
        """Select a target and then return the utility
        of performing this action on that target"""
        if not self.__targets:
            return -math.inf

        target_utilities = self._get_target_utilities()

        if self.selection_method == SelectionMethod.MAX:
            return self._max_selection(target_utilities)
        if self.selection_method == SelectionMethod.WEIGHTED_RANDOM:
            return self._weighted_random_selection(target_utilities)

        raise ValueError('Target selection method not recognized')

    def verify_targets(self, targets: TargetStats,
                       nodes: Dict[str, UtilityGraphNode]):
        if not targets:
            return

        self._verify_target_stats(targets, nodes)

    def _verify_target_stats(self, targets: TargetStats,
                             nodes: Dict[str, UtilityGraphNode]):
        stat_names = [n for n, v in targets[0].items()]
        self.stat_nodes = {}
        for stat_name in stat_names:
            for t in targets:
                if stat_name not in t:
                    raise ValueError('Every target dict must have the same keys')

            if stat_name not in nodes and stat_name != 'key':
                raise NodeNotFoundError("Can't find stat node with name: "
                                        + stat_name)
            elif stat_name != 'key':
                node = nodes[stat_name]

                if isinstance(node, StatNode):
                    self.stat_nodes[stat_name] = node
                else:
                    raise NodeTypeError('The stat names supplied when updating target_stats \
                    for a TargetActionNode must correspond to a StatNode in the \
                    same graph')

    def _get_target_utilities(self) -> List[float]:
        """Determine what the utility of this action
        would be for each possible target"""
        target_utilities = []

        for t in self.targets:
            for stat_name, stat_val in t.items():
                if stat_name != 'key':
                    stat_node = self.stat_nodes[stat_name]
                    stat_node.set_value(stat_val)

            target_utilities.append(ActionNode.output.fget(self))
            self.reset()

        return target_utilities

    def _max_selection(self, target_utilities: List[float]) -> float:
        """Select that target that results in the highest possible
        utility for this action"""
        util = max(target_utilities)
        self.target_index = target_utilities.index(util)
        return util

    def _weighted_random_selection(self, target_utilities: List[float]) \
            -> float:
        """Randomly select a target from the top_subset_size target_stats
        that result in the highest utility for this action. Weight
        the selection based on resulting utility."""
        index_util = list(zip(range(self.num_targets), target_utilities))
        selected = select_weighted_random(index_util,
                                          self.top_subset_size,
                                          lambda iu: iu[1])
        self.target_index = selected[0]
        return selected[1]
