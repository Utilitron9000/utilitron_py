from graph.math_nodes.reducer_node import ReducerNode


class MinNode(ReducerNode):
    """Node representing a minimization operation"""
    def __init__(self):
        super().__init__(lambda x, y: min(x, y))
