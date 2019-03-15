from .reducer_node import ReducerNode

class MultiplicationNode(ReducerNode):
    """Node representing a multiplication operation"""
    def __init__(self):
        ReducerNode.__init__(self, lambda x, y: x * y)