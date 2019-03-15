from .reducer_node import ReducerNode

class MinNode(ReducerNode):
    """Node representing a minimization operation"""
    def __init__(self):
        ReducerNode.__init__(self, lambda x, y: min(x, y))