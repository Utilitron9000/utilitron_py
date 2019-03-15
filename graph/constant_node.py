from .utility_graph_node import UtilityGraphNode

class ConstantNode(UtilityGraphNode):
    """Node representing a possible action available to the agent"""
    def __init__(self, value: float):
        UtilityGraphNode.__init__(self)
        self.max_inputs = 0
        self.output_val = value

    def set_value(self, value):
        self.output_val = value

    def reset(self):
        pass
