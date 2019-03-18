from graph.math_nodes.reducer_node import ReducerNode


class DivisionNode(ReducerNode):
    """Node representing a division operation"""
    def __init__(self):
        super().__init__(lambda x, y: x / y)
