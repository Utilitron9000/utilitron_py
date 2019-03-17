from graph.math_nodes.reducer_node import ReducerNode


class AdditionNode(ReducerNode):
    """Node representing an addition operation"""
    def __init__(self):
        ReducerNode.__init__(self, lambda x, y: x + y)
