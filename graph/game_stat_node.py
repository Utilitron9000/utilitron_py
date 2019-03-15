from .utility_graph_node import UtilityGraphNode

class GameStatNode(UtilityGraphNode):
    """Node representing a possible action available to the agent"""
    def __init__(self, name: str):
        UtilityGraphNode.__init__(self)
        self.name = name
        self.max_inputs = 0

    def set_value(self, value):
        self.output_val = value

    def reset(self):
        pass
