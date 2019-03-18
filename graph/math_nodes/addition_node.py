from graph.math_nodes.reducer_node import ReducerNode


class AdditionNode(ReducerNode):
    """Node representing an addition operation"""
    def __init__(self):
        super().__init__(lambda x, y: x + y)
