from typing import List, Tuple
from uuid import UUID
from .action_node import ActionNode
from enum import Enum
import random

ActionKV = Tuple[UUID, ActionNode]


class UtilityGraph:
    def __init__(self, seed):
        self.nodes = {}
        self.actions = {}
        self.selection_method = SelectionMethod.MAX
        self.top_subset_size = 3
        random.seed(seed)

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
        return max(self.actions.items(), key=lambda kv: kv[1].output)[1]

    def _weighted_random_selection(self) -> Tuple[str, float]:
        """Performs a weighted random selection on the 'top_subset_size' actions with
        the highest utility values."""
        top_actions = self._weight_actions_by_utility(self._get_top_actions())

        return top_actions[self.rand_gen.randint(0, len(top_actions) - 1)][1]

    def _weight_actions_by_utility(self, actions: List[ActionKV]) \
            -> List[ActionKV]:
        """Given a list of actions with normalized utility values (0-1)
        return a list where an action with utility value n appears
        100n times in the list"""
        extended_by_weight = [[kv] * int(kv[1].output * 100)
                              for kv in actions]
        return [kv for sublist in extended_by_weight for kv in sublist]

    def _get_top_actions(self) -> List[Tuple[ActionKV]]:
        """Get the 'top_subset_size' actions with the highest
        utility values"""
        sorted_actions = sorted([(k, v) for k, v in self.actions.items()],
                                reverse=True,
                                key=lambda kv: kv[1].output)
        return sorted_actions[:self.top_subset_size]


