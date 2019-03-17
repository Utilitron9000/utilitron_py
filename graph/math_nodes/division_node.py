from graph.math_nodes.reducer_node import ReducerNode


class DivisionNode(ReducerNode):
    """Node representing a division operation"""
    def __init__(self):
        ReducerNode.__init__(self, lambda x, y: x / y)
