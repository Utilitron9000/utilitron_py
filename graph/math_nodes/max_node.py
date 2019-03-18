from graph.math_nodes.reducer_node import ReducerNode


class MaxNode(ReducerNode):
    """Node representing a minimization operation"""
    def __init__(self):
        super().__init__(lambda x, y: max(x, y))
