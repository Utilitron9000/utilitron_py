from graph.math_nodes.reducer_node import ReducerNode


class MultiplicationNode(ReducerNode):
    """Node representing a multiplication operation"""
    def __init__(self):
        super().__init__(lambda x, y: x * y)
