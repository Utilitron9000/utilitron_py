import math
from functools import reduce
from typing import Callable
from ..utility_graph_node import UtilityGraphNode, NodeConnectionError


class ReducerNode(UtilityGraphNode):
    """Node representing a mathematical operation
    to be performed on each of the inputs
    in order to reduce them to a single output value"""
    def __init__(self, operation: Callable):
        UtilityGraphNode.__init__(self)
        self.max_inputs = math.inf
        self.operation = operation

    def get_output(self):
        if self.output:
            return self.output

        if not self.connected_inputs:
            raise NodeConnectionError("""A reducer node must have at least
            one connected input to produce an output""")

        connected_input_vals = [i.output for i in self.connected_inputs]
        self.output = reduce(self.operation, connected_input_vals)

        return self.output
