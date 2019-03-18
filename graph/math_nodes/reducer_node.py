import math
from functools import reduce
from typing import Callable
from graph.utility_graph_node import UtilityGraphNode, NodeConnectionError


class ReducerNode(UtilityGraphNode):
    """Node representing a mathematical operation
    to be performed on each of the inputs
    in order to reduce them to a single output value"""
    def __init__(self, operation: Callable):
        super().__init__()
        self.max_inputs = math.inf
        self.operation = operation

    @UtilityGraphNode.output.getter
    def output(self):
        if not self.connected_inputs:
            raise NodeConnectionError("""A reducer node must have at least
            one connected input to produce an output""")

        if self._output:
            return self._output

        connected_input_vals = [i.output for i in self.connected_inputs]
        self._output = \
            reduce(self.operation, connected_input_vals)

        return self._output
