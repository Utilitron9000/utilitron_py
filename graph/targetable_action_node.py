import math
from typing import Dict, List
from graph.action_node import ActionNode
from graph.stat_node import StatNode
from graph.selection import select_weighted_random, SelectionMethod
from graph.utility_graph_node import UtilityGraphNode
from graph.exceptions import NodeNotFoundError, NodeTypeError

TargetStats = Dict[str, List[float]]


class TargetableActionNode(ActionNode):
    """Node representing a possible action available to an agent
    that can be performed on a number of different targets"""
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
        if not targets:
            self.__targets = {}
            self.num_targets = 0
            self.target_index = -1

        # Get the length of an arbitrary value of the targets dict
        self.num_targets = len(next(iter(targets.values())))

        self.__targets = targets

    @ActionNode.output.getter
    def output(self) -> float:
        """Select a target and then return the utility
        of performing this action on that target"""
        if self.num_targets <= 0:
            return -math.inf

        target_utilities = self._get_target_utilities()

        if self.selection_method == SelectionMethod.MAX:
            return self._max_selection(target_utilities)
        if self.selection_method == SelectionMethod.WEIGHTED_RANDOM:
            return self._weighted_random_selection(target_utilities)

        raise ValueError('Target selection method not recognized')

    def verify_target_stats(self, targets: TargetStats,
                            nodes: Dict[str, UtilityGraphNode]):
        self.stat_nodes = {}

        last_len = None
        for stat_name, stat_vals in targets.items():
            if last_len is not None and len(stat_vals) != last_len:
                raise ValueError('When updating targets for an action \
                all stats must have a value for each target')
            last_len = len(stat_vals)

            if stat_name not in nodes:
                raise NodeNotFoundError('Node '
                                        + stat_name + ' could not be found')

            node = nodes[stat_name]

            if isinstance(node, StatNode):
                self.stat_nodes[stat_name] = node
            else:
                raise NodeTypeError('The stat names supplied when updating targets \
                for a TargetActionNode must correspond to a StatNode in the \
                same graph')

    def _get_target_utilities(self) -> List[float]:
        """Determine what the utility of this action
        would be for each possible target"""
        target_utilities = []

        for i in range(self.num_targets):
            # Set the stat values for target i
            for stat_name, stat_vals in self.targets.items():
                stat_node = self.stat_nodes[stat_name]
                stat_node.set_value(stat_vals[i])

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
        """Randomly select a target from the top_subset_size targets
        that result in the highest utility for this action. Weight
        the selection based on resulting utility."""
        index_util = list(zip(range(self.num_targets), target_utilities))
        selected = select_weighted_random(index_util,
                                          self.top_subset_size,
                                          lambda iu: iu[1])
        self.target_index = selected[0]
        return selected[1]
