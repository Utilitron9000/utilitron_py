from uuid import uuid4


class UtilityGraphNode:
    """The base class for all utility graph nodes"""
    def __init__(self):
        self.max_inputs = 1
        self.connected_inputs = []
        self.id = str(uuid4())
        self.__output = None

    @property
    def output(self):
        """Get the output value of this node"""
        return self.__output

    def connect_input(self, node):
        """Connect another UtilityGraphNode as an input to this node"""
        if len(self.connected_inputs) + 1 <= self.max_inputs:
            self.connected_inputs.append(node)
        else:
            raise NodeConnectionError()

    def reset(self):
        self.__output = None
        for i in self.connected_inputs:
            i.reset()


class NodeConnectionError(Exception):
    """Exception thrown when an invalid connection is attempted"""
    pass
