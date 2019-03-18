from graph.utility_graph_node import UtilityGraphNode


class StatNode(UtilityGraphNode):
    """Node representing a gameplay statistic
    such as an agent's health"""
    def __init__(self, name: str):
        super().__init__()
        self.name = name
        self.id = name
        self.max_inputs = 0

    def set_value(self, value):
        self._output = value

    def reset(self):
        pass
