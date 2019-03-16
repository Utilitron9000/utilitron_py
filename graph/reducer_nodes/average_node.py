from .reducer_node import ReducerNode

class AverageNode(ReducerNode):
    """Node representing an average operation"""
    def __init__(self):
        ReducerNode.__init__(self, lambda x, y: x + y)

    def get_output(self):
        sum = ReducerNode.get_output(self)
        self.output = sum/len(self.connected_inputs)
        return self.output
