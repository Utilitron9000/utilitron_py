from graph.utility_graph_node import UtilityGraphNode


class StatNode(UtilityGraphNode):
    """Node representing a gameplay statistic
    such as an agent's health"""
    def __init__(self, name: str):
        UtilityGraphNode.__init__(self)
        self.name = name
        self.max_inputs = 0

    def set_value(self, value):
        self._UtilityGraphNode__output = value

    def reset(self):
        pass
