from uuid import uuid4

class UtilityGraphNode:
    """The base class for all utility graph nodes"""
    def __init__(self):
        self.max_inputs = 1
        self.connected_inputs = []
        self.id = uuid4()
        self.output_val = None

    def get_output(self):
        """Get the output value of this node"""
        return self.output_val

    def connect_input(self, node: 'UtilityGraphNode'):
        """Connect a node as an input to this node"""
        if len(self.connected_inputs) + 1 <= self.max_inputs:
            self.connected_inputs.append(node)
        else:
            raise NodeConnectionError()

    def reset(self):
        self.output_val = None

class NodeConnectionError(Exception):
    """Exception thrown when an invalid connection is attempted"""
    pass

