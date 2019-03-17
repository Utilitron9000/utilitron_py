from graph.math_nodes.reducer_node import ReducerNode


class MaxNode(ReducerNode):
    """Node representing a minimization operation"""
    def __init__(self):
        ReducerNode.__init__(self, lambda x, y: max(x, y))
