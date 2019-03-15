from .utility_graph_node import UtilityGraphNode

class ScoreNode(UtilityGraphNode):
    """Node representing a possible action available to the agent"""
    def __init__(self, name: str):
        UtilityGraphNode.__init__(self)
        self.name = name
        self.max_inputs = 1

    def get_output(self):
        return self.connected_inputs[0].output_val if self.connected_inputs else None
