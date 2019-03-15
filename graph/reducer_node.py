import math
from functools import reduce
from typing import Callable
from .utility_graph_node import UtilityGraphNode

class ReducerNode(UtilityGraphNode):
    """Node representing a possible action available to the agent"""
    def __init__(self, operation: Callable):
        UtilityGraphNode.__init__(self)
        self.max_inputs = math.inf
        self.operation = operation

    def get_output(self):
        if self.output_val:
            return self.output_val

        if not self.connected_inputs:
            raise ValueError("""A reducer node must have at least
            one connected input to produce an output""")

        connected_input_vals = [i.output_val for i in self.connected_inputs]
        self.output_val = reduce(self.operation, connected_input_vals)

        return self.output_val
