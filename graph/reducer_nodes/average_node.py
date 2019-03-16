from .reducer_node import ReducerNode
from ..utility_graph_node import UtilityGraphNode


class AverageNode(ReducerNode):
    """Node representing an average operation"""
    def __init__(self):
        ReducerNode.__init__(self, lambda x, y: x + y)

    @UtilityGraphNode.output.getter
    def output(self):
        sum = ReducerNode.output.fget(self)
        self._UtilityGraphNode__output = sum/len(self.connected_inputs)
        return self._UtilityGraphNode__output
