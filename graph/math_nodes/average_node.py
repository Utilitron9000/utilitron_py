from graph.math_nodes.reducer_node import ReducerNode
from graph.utility_graph_node import UtilityGraphNode


class AverageNode(ReducerNode):
    """Node representing an average operation"""
    def __init__(self):
        super().__init__(lambda x, y: x + y)

    @UtilityGraphNode.output.getter
    def output(self):
        sum = ReducerNode.output.fget(self)
        self._output = sum/len(self.connected_inputs)
        return self._output
