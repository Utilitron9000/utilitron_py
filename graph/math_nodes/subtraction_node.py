from graph.math_nodes.reducer_node import ReducerNode


class SubtractionNode(ReducerNode):
    """Node representing a subtraction operation"""
    def __init__(self):
        ReducerNode.__init__(self, lambda x, y: x - y)
