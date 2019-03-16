from .utility_graph_node import UtilityGraphNode


class ScoreNode(UtilityGraphNode):
    """A named node that simply repeats
    its input value to its output"""
    def __init__(self, name: str):
        UtilityGraphNode.__init__(self)
        self.name = name
        self.id = name
        self.max_inputs = 1

    @UtilityGraphNode.output.getter
    def output(self):
        if self.connected_inputs:
            return self.connected_inputs[0].output
        else:
            return None
