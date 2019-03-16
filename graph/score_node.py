from .utility_graph_node import UtilityGraphNode


class ScoreNode(UtilityGraphNode):
    """A named node that simply repeats
    its input value to its output"""
    def __init__(self, name: str):
        UtilityGraphNode.__init__(self)
        self.name = name
        self.max_inputs = 1

    def get_output(self):
        if self.connected_inputs:
            return self.connected_inputs[0].get_output()
        else:
            return None
